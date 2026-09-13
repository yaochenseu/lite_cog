# LSLIDAR_CX_V4.2.0_220823_ROS

## 1.Introduction

​		LSLIDAR_CX_V4.2.0_220823_ROS is the lidar ros driver in linux environment, which is suitable for C1,C8,C16 and C32(32 degrees,70 degrees,90 degrees)  lidar. The program has  tested under ubuntu 20.04 ros noetic and ubuntu18.04 ros melodic.

## 2.Dependencies

1.ros

To run lidar driver in ROS environment, ROS related libraries need to be installed.

**Ubuntu 16.04**: ros-kinetic-desktop-full

**Ubuntu 18.04**: ros-melodic-desktop-full

**Ubuntu 20.04**: ros-noetic-desktop-full

**Installation**: please refer to [http://wiki.ros.org]

2.ros dependencies

```bash
# install
sudo apt-get install ros-$ROS_DISTRO-pcl-ros ros-$ROS_DISTRO-pluginlib  ros-$ROS_DISTRO-pcl-conversions  ros-$ROS_DISTRO-diagnostic-updater
```

3.other dependencies

~~~bash
sudo apt-get install libpcap-dev
~~~

## 3.Compile && Run

### 3.1 Compile

~~~bash
mkdir -p ~/lidar_ws/src
~~~

Copy the whole lidar ROS driver directory into ROS workspace, i.e "~/lidar_ws/src".

~~~bash
cd ~/lidar_ws
catkin_make
source devel/setup.bash
~~~

3.2 Run

run with single lidar:

~~~bash
# C1
roslaunch lslidar_driver lslidar_c1.launch
# C8
roslaunch lslidar_driver lslidar_c8.launch
# C16
roslaunch lslidar_driver lslidar_c16.launch
# C32
roslaunch lslidar_driver lslidar_c32.launch
~~~

run with double lidar:

~~~bash
roslaunch lslidar_driver lslidar_double.launch
~~~



## 4. Introduction to parameters

The content of the lslidar_c32.launch file is as follows, and the meaning of each parameter is shown in the notes.

~~~bash
<launch>
  <arg name="device_ip" default="192.168.1.200" />           #lidar ip
  <arg name="msop_port" default="2368"/>                     # Main data Stream Output Protocol packet port
  <arg name="difop_port" default="2369"/>                    # Device Information Output Protocol packet port
  <arg name="use_gps_ts" default="false" />                  # Whether gps time synchronization
  <arg name="pcl_type" default="false" />                    # pointcloud type，false: xyzirt,true:xyzi
  <arg name="lidar_type" default="c32"/>                     # lidar type c1 or c8 or c16 or c32
  <arg name="c32_type" default="c32_32"/>                    #<!--c32_32: The vertical angle is 30 degrees  c32_70: The vertical angle is 70 degrees   c32_90: The vertical angle is 90 degrees /-->
  <arg name="packet_rate" default="1695.0"/>                 #The number of data packets sent by the lidar per second. This parameter is useful when reading pcap packets

  <node pkg="lslidar_driver" type="lslidar_driver_node" name="lslidar_driver_node" output="screen">
    <!--param name="pcap" value="$(find lslidar_driver)/pcap/123.pcap" /-->   #Uncomment to read the data from the pcap file, and add the comment to read the data from the lidar
    <param name="packet_rate" value="$(arg packet_rate)"/>           
    <param name="device_ip" value="$(arg device_ip)" />
    <param name="msop_port" value="$(arg msop_port)" />
    <param name="difop_port" value="$(arg difop_port)"/>
    <param name="pcl_type" value="$(arg pcl_type)"/>         # pointcloud type，false: xyzirt,true:xyzi
    <param name="lidar_type" value="$(arg lidar_type)"/>     # lidar type c1 or c8 or c16 or c32
    <param name="c32_type" value="$(arg c32_type)"/>         
    <param name="add_multicast" value="false"/>               #  Whether to add multicast
    <param name="group_ip" value="224.1.1.2"/>                 #multicast ip
    <param name="use_gps_ts" value="$(arg use_gps_ts)"/>       
    <param name="min_range" value="0.15"/>                    #Unit: m. The minimum value of the lidar blind area, points smaller than this value are filtered
    <param name="max_range" value="150.0"/>                   #Unit: m. The maximum value of the lidar blind area, points smaller than this value are filtered
    <param name="frame_id" value="laser_link"/>                # lidar point cloud coordinate system name
    <param name="distance_unit" value="0.40"/>                 #lidar range resolution
    <param name="angle_disable_min" value="0"/>               #lidar clipping angle start value ，unit:0.01°
    <param name="angle_disable_max" value="0"/>               #lidar clipping angle end value ，unit:0.01°
     <param name="horizontal_angle_resolution" value="0.2"/>   # Horizontal angle resolution 10Hz:0.2  20Hz:0.4 5Hz: 0.1 
    <param name="scan_num" value="10"/>                       #laserscan line number
    <param name="read_once" value="false"/>                   #Whether to play the pcap package repeatedly, false: play it repeatedly true: play it only once
    <param name="publish_scan" value="false"/>               #Whether to publish the scan
    <param name="pointcloud_topic" value="lslidar_point_cloud"/>  #point cloud topic name, can be modified
    <param name="coordinate_opt" value="false"/>             #Default false. The zero degree angle of the lidar corresponds to the direction of the point cloud
  </node>

  <node pkg="rviz" type="rviz" name="rviz" args="-d $(find lslidar_driver)/rviz_cfg/lslidar.rviz"/>
  
 <!--node pkg="tf" type="static_transform_publisher" name="laser_link_to_world" args="0 0 0 0 0 0 world laser_link 100" /-->
</launch>
~~~

- ### Multicast mode:

  - The host computer sets the lidar to enable multicast mode

  - Modify the following parameters of the launch file

  ~~~shell
  <param name="add_multicast" value="true"/>                 #add multicast
  <param name="group_ip" value="224.1.1.2"/>                 # The multicast ip address set by the host computer
  ~~~

- Run the following command to add the computer to the group (replace enp2s0 in the command with the network card name of the user's computer, you can use ifconfig to view the network card name)

  ~~~shell
  ifconfig
  sudo route add -net 224.0.0.0/4 dev enp2s0
  ~~~



- ### Offline pcap mode:

  - Copy the recorded pcap file to the lslidar_ros/lslidar_driver/pcap folder
  
  - Modify the following parameters of the launch file
  
  ~~~shell
  // uncomment
      <param name="pcap" value="$(find lslidar_driver)/pcap/123.pcap" /> 
  ~~~

- ### pcl point cloud type:

  - Modify the following parameters of the launch file

  ~~~shell
  <param name="pcl_type" value="$(arg pcl_type)"/>          # pointcloud type，false: xyzirt,true:xyzi
  ~~~

- The default false is the custom point cloud type, which references the definition in the file of

  lslidar_driver/include/lslidar_driver.h

  Change it to true, which is the own type of pcl:

  ~~~c++
  pcl::PointCloud<pcl::PointXYZI>
  ~~~

## FAQ

Bug Report

Original version : LSLIDAR_CX_V4.1.4_220425_ROS

Modify:  original version

Date    : 2022-04-25

--------------------------------------------------------------------

Original version : LSLIDAR_CX_V4.1.5_220620_ROS

Modify: Modify the optical vertical angle.

Date    : 2022-06-20

------------------------------------------------------------

Original version : LSLIDAR_CX_V4.2.0_221028_ROS

Modify:  1. Added support for version 4.0 single line lidar and C32 70 degree and 90 degree lidars

2.Unify laserscan and pointcloud2 coordinate systems

Date    : 2022-10-28
