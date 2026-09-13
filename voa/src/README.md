## 地形图与可通行区域

### 源码编译

1. 先编译kindr、kindr_msgs、kindr_ros功能包
2. 再编译其他功能包

### 输入输出

#### 输入

* 点云话题（对深度相机和激光雷达进行区分输入）

  ROS话题：话题名称可自定义，见后面参数配置说明

  消息类型：sensor_msgs::PointCloud2

* 机器人位姿tf（默认IMU的位姿）

  /world->/base_link（可在参数配置中自定义，若/base_link改变，launch文件中的外参静态tf也需调整，包括身体到相机，身体到激光雷达）

#### 输出

* 地形图
    ROS话题：/deeprobotics_local_height_map/height_map
    消息类型：grid_map_msgs::GridMap
    图层：elevation(高度)、color（颜色）、slope（坡度）、accessibility（可通行区域）
    补充说明：可通行区域层中，有高度信息且可踩格为0.0,空格为0.01,不可踩但可通行格为0.1,不可通行格为1.0,在访问时，因为是double类型，请用>和<比较符号来判断格子属性，请勿直接使用==号判断

### 启动方法

* Mini：

```bash
$ cd height_map_ws
$ source devel/setup.bash
$ roslaunch height_map_mini.launch
```

* X20：

```bash
$ cd height_map_ws
$ source devel/setup.bash
$ roslaunch height_map_x20.launch
```

### 参数配置

在要开启的launch文件中可配置以下关键参数：

```launch
<!-- 相机竖放或平放 vertical or horizontal -->
<arg name="camera_pose" default="vertical" />
<!-- 是否打开可视化界面Rviz --> 
<arg name="enable_rviz" default="true" />
<!-- 是否打开机器人urdf模型 -->
<arg name="enable_urdf" default="true" />
<!-- 是否在Rviz中显示足底轨迹 -->
<arg name="enable_joint_path" default="false" />
<!-- 是否打开运动传输程序 -->
<arg name="enable_transformer" default="false" />
<!-- 是否使用数据集运行（且没有相机tf） -->
<arg name="enable_camera_optical_tf" default="true" />
<!-- 是否打开地形图传输程序 -->
<arg name="enable_gridmap_transformer" default="false" />
```

在param_all_camera_v.yaml（若launch文件中camera_pose参数为vertical）或param_all_camera_h.yaml（若launch文件中camera_pose参数为horizontal）中可配置以下重要参数：

```yaml
thread_number: 3   #输入多少点云话题就设置多少线程数，设得比点云话题多会明显增加cpu占用
point_cloud_topic_lidar: "/rslidar_points"  #激光雷达点云
point_cloud_topic: "/camera_front_left/depth/color/points"  #深度相机点云，最多可配置5个，point_cloud_topic～point_cloud_topic5
point_cloud_topic2: "/camera_front_right/depth/color/points"
map_frame_id: "world"  #世界坐标系
robot_base_frame_id: "base_link"  #机器人身体坐标系
track_point_frame_id: "/base_link"  #地图中心跟踪的坐标系（跟位置不跟姿态）
length_in_x: 3.0   # 地形图尺寸（目前地形分析100×100网格，改动可能会出现问题，3×3m用于落脚点，5×5m可用于导航局部地图）
length_in_y: 3.0
resolution: 0.03
addPointMethod: 1   # 使用场景 1:普通  2:工业楼梯
height_filter: 1    # 高度层腐蚀膨胀法滤波  1:开  2：关  落脚点地图需要打开使高度面更平滑，并避免下楼梯时自己的脚的点云影响地图，但同时会导致占用格子少的细小障碍物被过滤掉
# 可通行区域参数
stand_height: 0.38 #机器狗站立高度  #mini站立高度：0.38    x20站立高度：0.48
step_z_max: 0.2   #认为可通行的台阶高度，一般要设置的比实际台阶大，因为地形建图存在误差，由于不同步态对应的高度不同，该参数开放了ros话题输入接口
step_forward_max: 0.23   #足式机器人最大步长，5×5地图需要设置偏大，如0.3
slope_threshold: 0.839   #认为不可踩的坡度阈值
slope_inflation: 1.1    #需要进行膨胀的坡度阈值，主要是为了膨胀楼梯边缘
```

* 动态调整可通行台阶高度step_z_max

  ROS话题：/step_z_max

  消息类型：std_msgs/Float64
