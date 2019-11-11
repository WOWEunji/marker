#!/usr/bin/python3
# -*- coding: utf=8 -*-

import numpy as np
import cv2
from cv2 import aruco

frame = cv2.imread("~/Project/aruco/_data/Screenshot from 2019-11-11 13-49-55.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
parameters =  aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
print(ids)
