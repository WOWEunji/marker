# marker

get id from aruco_maker

## features

* get_aruco marker id

* wrapper with ros kinetic


## test with realsense r200

ros service
```
roslaunch realsense_camera r200_nodelet_rgbd.launch
rosrun marker marker_detector.py
```

ros client
```
rosrun request.py
```
