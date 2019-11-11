#!/usr/bin/env python

import sys
import rospy
from marker.srv import Recogresult

def Recognition(str):
    print(str)
    rospy.wait_for_service('marker_recog')
    try:
        marker_recog = rospy.ServiceProxy('marker_recog', Recogresult)
        print("ab")
        resp1 = marker_recog(str)
        return resp1.objid
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print(Recognition("start"))
