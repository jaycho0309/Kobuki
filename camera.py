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
global imageno
imageno = 0

def callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding ='bgr8') # passthrough #32FC1
    global imageno   
    _path_ = '' if imageno ==0 else 'data/' 
    cv2.imwrite('/home/cilab/yolov3/%srealsense_video%d.jpg'%(_path_, imageno), cv_image) # Program dead if overwrithe one image
    cv2.waitKey(12) # The image refresh for every 90ms. 
    imageno += 1
    if imageno == 8:
        imageno = 0


def listener():
    rospy.init_node('cam')
    rospy.Subscriber('/camera/color/image_raw', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
