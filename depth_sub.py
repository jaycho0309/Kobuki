#!/usr/bin/env python
import rospy
import rospkg
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Int32, Int32MultiArray, MultiArrayLayout, MultiArrayDimension
from cv_bridge import CvBridge, CvBridgeError
import sys
import matplotlib.pyplot as plt

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages') # in order to import cv2 under python3
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages') # append back in order to import rospy
from time import sleep
#from cv_bridge.boost.cv_bridge_boost import getCvType

bridge = CvBridge()
#pub_person = rospy.Publisher('person', Int32, queue_size = 10)
pub_redzone = rospy.Publisher('redzone', Int32MultiArray, queue_size = 10)

def callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding ='passthrough') # passthrough #32FC1
    #r = Int32MultiArray()
    #redzone = MultiArrayDimension()
    #redzone.label = 'x'
    #redzone.size = 170
    #redzone.stride = 1
    redzone = cv_image.reshape(-1) 
    #redzone = cv_image[400][312:537]
    #redzone  
    r = Int32MultiArray(data = redzone)
    
    #cv2.imshow("window", cv_image)
    #cv2.waitKey(1)
    print r.data[848*360+312:848*360+536]
    pub_redzone.publish(r)
    #rospy.sleep(1)

def listener():
    rospy.init_node('DepthSubscriber')
    rospy.Subscriber('/camera/depth/image_rect_raw', Image, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    
