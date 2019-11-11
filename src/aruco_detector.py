#!/usr/bin/python3
# -*- coding: utf=8 -*-
import sys
import cv2
import numpy as np
import platform
print(platform.python_version())
from cv2 import aruco
from cv_bridge import CvBridge, CvBridgeError

print(cv2.__version__)

def getid(image_src):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(image_src, aruco_dict, parameters=parameters)
    if(ids is None):
        print("None!!!!")
        result = []
        result.append(0)
    else:
        print("cdcd")
        frame_markers = aruco.drawDetectedMarkers(image_src.copy(), corners, ids)
        # cv2.imshow('frame_result', frame_markers), cv2.waitKey(1)
        print(len(ids))
        print(ids)

        result = []
        for i in range(len(ids)):
            print(ids[i])
            result.append(ids[i][0])
    print(result)
    return result
