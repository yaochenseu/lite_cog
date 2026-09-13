开相机驱动
cd realsense-driver
source devel/setup.bash
roslaunch realsense2_camera tony_multiple_camera.launch

开传输程序（导航launch一般已启动）
cd deeprobotics_perception/drivers
source devel/setup.bash
roslaunch message_transformer_cpp message_transformer_cpp.launch

安全停避障
cd height_map_ws
source devel/setup.bash  
roslaunch deeprobotics_local_height_map height_map_safety.launch


