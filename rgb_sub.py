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

bridge = CvBridge()
pub_rgb = rospy.Publisher('rgb', Int32MultiArray, queue_size = 10)

def callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding ='bgr8') # passthrough #32FC1
    print np.shape(cv_image)
    rgb = cv_image.reshape(-1) 
    print np.shape(rgb)
    r = Int32MultiArray(data = rgb)

    pub_rgb.publish(r)
    #rospy.sleep(1)

def listener():
    rospy.init_node('RGBSubscriber')
    rospy.Subscriber('/camera/color/image_raw', Image, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    
