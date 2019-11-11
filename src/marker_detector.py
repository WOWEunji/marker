#!/usr/bin/env python
# -*- coding: utf=8 -*-

import rospy
import cv2
import numpy as np
import aruco_detector
#from cv2 import aruco
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from marker.srv import Recogresult

class Gray():
    def __init__(self):
        self.selecting_sub_image = "raw" # you can choose image type "compressed", "raw"

        self._sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.callback)

        self.bridge = CvBridge()

    def callback(self, image_msg):
        global cv_image
        cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")

        self.cv_gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
        # aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
        # parameters =  aruco.DetectorParameters_create()
        # corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        # frame_markers = aruco.drawDetectedMarkers(cv_gray.copy(), corners, ids)
        cv2.imshow('cv_gray', self.cv_gray), cv2.waitKey(1)

    def maker_callback(self, request):
        print("Request")
        global cv_image
        (row, col, channel1) = cv_image.shape
        img = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
        print("ab")
        result = aruco_detector.getid(img)
        return {'objid':result}


    def main(self):
        rospy.init_node('marker_recognition', anonymous=True)
        s = rospy.Service('marker_recog',Recogresult, self.maker_callback)
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down..")
            cv2.destroyAllWindows()

if __name__ == '__main__':
    node = Gray()
    node.main()
