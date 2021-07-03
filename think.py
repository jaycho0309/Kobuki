#!/usr/bin/env python


import rospy
import math
import time
import numpy as np
from kobuki_project.msg import Status
from std_msgs.msg import Int32, Int32MultiArray, MultiArrayLayout, MultiArrayDimension
from geometry_msgs.msg import Twist


rospy.init_node('front_viewer')
pub = rospy.Publisher('/kobuki_velocity', Twist, queue_size = 1)
rate = rospy.Rate(5)
move = Twist()
global speed
speed = 0.2
angle = 0.1

global action # -1: BACK 0:STOP  1:GO  2:LEFT  3:RIGHT  
action = 1
global DDD
DDD = 0
def front_view(depth): # [312 - 536]   
    global action
    global speed
    action = 0
    cnt = 0
    cnt_left = 0
    cnt_right = 0
    center_person_x = 0.5
    target_person_check = 9999999
    human_in_redzone = [0,0] # human position [left, right] in redzone
    yolo_result = open('/home/cilab/yolov3/yoloresult.txt') # yoloresult.txt.
    lines = yolo_result.readlines()
    for line in lines:
	obj_cls, obj_x, obj_y, obj_w, obj_h = line.split(" ")
        if obj_cls == '0':
	    action = 1
            obj_x, obj_y, obj_w, obj_h = float(obj_x)*848, float(obj_y)*480, float(obj_w)*848, float(obj_h)*480
            obj_box = [int(obj_x - obj_w/2), int(obj_x + obj_w/2), int(obj_y - obj_h/2), int(obj_y + obj_h/2) ] # Left, right, top, bottom
	    dep = 0
	    rec_x, rec_y = int((obj_box[1] - obj_box[0]) / 3), int((obj_box[3] - obj_box[2]) / 3)  
            for i in range(rec_y):
		for j in range(rec_x):
		    dep += depth.data[848*(obj_box[2]+rec_y+i) + obj_box[0]+rec_x+j]  
            dep /= rec_x * rec_y
            if target_person_check > dep: # dep is closer than previous target
                target_person_check = dep 
		#print dep
                speed = min(max(0.2, float(dep)/4500 - 0.1), 0.5) # speed var
		#print speed		
		# dis < 1500: 0.2, dis > 3000: 0.5, between: Linear ==> min(max(0.2, float(dep)/5000 - 0.1), 0.5)
                center_person_x = obj_x / 848
                human_in_redzone = [obj_box[0], obj_box[1]] if (obj_box[2] <= 360 and obj_box[3] > 360) else [0,0]
     
    global DDD
    DDD = 0.5 - center_person_x # DDD = trun
     
    redzone = depth.data[848*360+312 : 848*360+536] # zikson rjfl
    yellowzone_L = depth.data[848*360+100 : 848*360+312] # sason rjfl
    yellowzone_R = depth.data[848*360+536 : 848*361-100]
    
    for i in range(len(redzone)):
        if redzone[i] < 1000 and redzone[i] > 0: # STOP
            cnt += 1
        
	if redzone[i] < 1500 and redzone[i] > 0: # TURN   
	    #if (((i+312) >= human_in_redzone[0]) and ((i+312) <= human_in_redzone[1])): # LRN
    		#continue   
	   # elif i < 112: # LEFT OBSTACLE; RIGHT TURN
    		  
	    if i < 112: # LEFT OBSTACLE; RIGHT TURN
    		cnt_right += 1
	    else:
		cnt_left += 1

    yellow_caution = [0,0] # Left, Right
    cnt_yellow_L = 0
    for i in range(len(yellowzone_L)):        
	if yellowzone_L[i] < 1500 and yellowzone_L[i] > 0: # TURN   
	    cnt_yellow_L +=1
    if cnt_yellow_L > 150:
	yellow_caution[0] = 1

    cnt_yellow_R = 0
    for i in range(len(yellowzone_R)):        
	if yellowzone_R[i] < 1500 and yellowzone_R[i] > 0: # TURN   
	    cnt_yellow_R +=1
    if cnt_yellow_R > 150:
	yellow_caution[1] = 1



    if cnt >= 10:  # Red stop
	action = -1
	#print "stop" 
    

    elif cnt_left >= 5 or cnt_right >= 5:
	if cnt_left >= cnt_right:
	    #print "Trun Left"
	    action = 3
	    #pass
	else:
	    #print "Turn Right"
	    action = 2
	    #pass

    if yellow_caution[0]: # Yellow_Left warning, go right or forward
	if action == 2: # If go left
	    action = 1 
	    print "Left warning" 
	if DDD < 0: # If turn left 
	    DDD = 0 
	    #print "Left warning"

    if yellow_caution[1]: # Yellow_Right warning, go left or forward
	if action == 3: # If go right
	    action = 1 
	    print "Right warning"
	if DDD > 0: # If turn right 
	    DDD = 0 
	    #print "Right warning"
    print action
    yolo_result.close()

def listener():
    rospy.init_node('front_viewer')
    rospy.Subscriber("redzone", Int32MultiArray, front_view)
    # spin() simply keeps python from exiting until this node is stopped
if __name__ == '__main__':
    listener()


while not rospy.is_shutdown():
## Open file
    '''
    yolo_result = open('/home/cilab/yolov3/yoloresult.txt') # yoloresult.txt.
    lines = yolo_result.readlines()


## Finding centermost person 
    center_person_x = 0 # X pos of TARGET person
    target_box = 0      # Target's box is largest
    for line in lines:
        obj_cls = int(line.split(" ")[0])
	obj_x = float(line.split(" ")[1])
	obj_w = float(line.split(" ")[3])
	obj_h = float(line.split(" ")[4])
	if obj_cls == 0: # if person
	    if target_box < obj_w * obj_h : # object size-based main object check
		target_box = obj_w * obj_h
		center_person_x = obj_x
    '''
## If person
    global DDD
    center_person_x = 0
    global action
    global speed

# move.angular.y: Force return
# move.linear.y : Force go straight

    if (action == 0 and move.angular.y and move.linear.y == 0):
	if move.angular.y == 0.02:
	    action = 3
	if move.angular.y == 0.03:
	    action = 2

    if action == -1: # BACK
	if (move.linear.x > 0.2 * -0.25):
		move.linear.x -= 0.04 
        move.angular.z = 0.0  
	#DDD = 0.0
    elif action == 2:
  	if (move.linear.x > speed):                     # Yes person, too close
            pass #move.linear.x -= 0.04
	if move.angular.y == 0.03:
	    move.angular.z = -0.05
  	    if (move.linear.x > speed):                     # Yes person, too close
                move.linear.x -= 0.02
	else:
	    move.angular.z = -0.4
	    move.linear.y += 1
	    move.angular.y = 0.02
    elif action == 3:
  	if (move.linear.x > speed):                     # Yes person, too close
            pass# move.linear.x -= 0.04
	if move.angular.y == 0.02:
	    move.angular.z = 0.05
  	    if (move.linear.x > speed):                     # Yes person, too close
                move.linear.x -= 0.02
	else:
	    move.angular.z = 0.4
	    move.linear.y += 1
	    move.angular.y = 0.03
    elif move.linear.y:
	if (move.linear.x < speed):                     # Yes person, too far
            move.linear.x += 0.02
  	if (move.linear.x > speed):                     # Yes person, too close
            move.linear.x -= 0.04  
            #DDD = 0.5 - center_person_x # DDD = trun
   	move.angular.z = 0.0
	move.linear.y -= 1
    elif action == 0: # STOP
	if (move.linear.x > 0):
		move.linear.x -= 0.02
	if (move.linear.x <= 0):
		move.linear.x = 0.0 
        move.angular.z = 0.0 
    elif action == 1:  # GO
	#DDD = 0.0
	if (move.linear.x < speed):                     # Yes person, too far
            move.linear.x += 0.02
  	if (move.linear.x > speed):                     # Yes person, too close
            move.linear.x -= 0.04  
            #DDD = 0.5 - center_person_x # DDD = trun
   	move.angular.z = DDD * 2
	move.angular.y = 0
   
    pub.publish(move)
   # print move.angular.z
    #print(DDD) # Check
#    yolo_result.close()  # Close yoloresult.txt.
    rate.sleep()

