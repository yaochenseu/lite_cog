 ## 1.地图目录：
 /home/ysc/lite_cog/system/map
 ## 2. 检查地图文件
  ls -lh /home/ysc/lite_cog/system/map
  lite3.pcd
  lite3.pgm
  lite3.yaml
 当前地图配置：

  image: /home/ysc/lite_cog/system/map/lite3.pgm
  resolution: 0.050000
  origin: [-2.350000, -3.750000, 0.00]
  negate: 0
  occupied_thresh: 0.65
  free_thresh: 0.196
 ## 3. 当前地图尺寸及范围

  当前栅格地图：

  width: 183
  height: 179
  resolution: 0.05 m/pixel

  实际地图范围约为：

  宽度：183 × 0.05 = 9.15 m
  高度：179 × 0.05 = 8.95 m

  地图坐标范围：

  左下角：(-2.35, -3.75)
  右上角：( 6.80,  5.20)

  地图坐标原点 (0,0) 在 PGM 图片中的大致位置：

  距离图片左边：47 像素
  距离图片底部：75 像素

  ———

  ## 4. ROS 地图坐标方向

  本工程中，Faster-LIO 建图起始位置近似为地图坐标 (0,0)。

  导航配置的初始位姿为：

  x = 0
  y = 0
  z = 0
  yaw = 0

  因此，建图开始时：

  +X：机器人前方
  -X：机器人后方
  +Y：机器人左方
  -Y：机器人右方

  示意图：

                    +Y（左侧）
                        ↑
                        |
                        |
  后方 -X  ←───────── (0,0) ─────────→  +X 前方
                        |
                        |
                        ↓
                    -Y（右侧）

  注意：

  - 这些方向不代表地理上的东、南、西、北。
  - 地图方向由开始建图时机器人的朝向决定。
  - 在 RViz 中应以坐标轴为准，不要仅凭图片上下左右判断。
  - RViz 中红色轴为 +X，绿色轴为 +Y，蓝色轴为 +Z。

  ———

  ## 5. 启动地图服务器

  打开终端：

  source /opt/ros/noetic/setup.bash
  source /home/ysc/lite_cog/slam/devel/setup.bash

  rosrun map_server map_server \
    /home/ysc/lite_cog/system/map/lite3.yaml

  保持该终端运行。

  如果提示无法连接 ROS Master，先在单独终端运行：

  roscore

  通常 Lite3 的系统服务已经提供 ROS Master，不需要重复启动。

  ———

  ## 6. 验证 /map 是否正常发布

  另开终端：

  source /opt/ros/noetic/setup.bash

  rostopic info /map

  正常应显示：

  Type: nav_msgs/OccupancyGrid

  Publishers:
   * /map_server_...

  检查地图信息：

  rostopic echo -n 1 /map/info

  当前地图的正常输出应包含：

  resolution: 0.05000000074505806
  width: 183
  height: 179
  origin:
    position:
      x: -2.35
      y: -3.75
      z: 0.0
    orientation:
      x: 0.0
      y: 0.0
      z: 0.0
      w: 1.0

  此时如果 Subscribers: None，仅表示 RViz 尚未订阅地图，不代表地图错误。

  ———

  ## 7. 临时建立 map → odom TF

  map_server 只发布 /map，不会发布 map → odom TF。

  因此，单独查看地图时，RViz 可能出现：

  Global Status: Error
  Fixed Frame [map] does not exist

  同时，Axes 的 Reference Frame 可能只有：

  <Fixed Frame>
  odom
  base_link

  为了查看地图坐标轴，打开新终端运行：

  source /opt/ros/noetic/setup.bash

  rosrun tf2_ros static_transform_publisher \
    0 0 0 0 0 0 map odom \
    __name:=map_to_odom_view

  保持该终端运行。

  此命令临时建立：

  map → odom → base_link

  该变换仅用于查看地图，不代表机器人已经完成真实定位。

  ———

  ## 8. 启动 RViz

  打开新终端：

  source /opt/ros/noetic/setup.bash
  source /home/ysc/lite_cog/slam/devel/setup.bash

  rviz -d /home/ysc/lite_cog/slam/src/pcd2grid/rviz/config.rviz

  在 RViz 中进行以下设置。

  ### Global Options

  Fixed Frame: map

  ### Map

  Topic: /map

  ### Axes

  点击：

  Add → By display type → Axes

  设置：

  Reference Frame: map

  也可以选择：

  Reference Frame: <Fixed Frame>

  因为当前 Fixed Frame 已设置为 map。

  如果列表没有刷新，可以删除原来的 Axes，再重新添加。

  ———

  ## 9. 验证 TF 是否连通

  source /opt/ros/noetic/setup.bash

  timeout 5 rosrun tf tf_echo map base_link

  如果能连续输出平移和旋转数据，说明 TF 链已经连通：

  map → odom → base_link

  此时 RViz 应满足：

  Global Status: OK
  Map Status: OK

  ———

  ## 10. 判断地图质量

  在 RViz 中检查：

  - 墙体是否连续
  - 是否存在明显双墙或重影
  - 房间和走廊形状是否与现场一致
  - 是否出现大面积错误障碍
  - 可通行区域是否为白色
  - 障碍物是否为黑色
  - 未知区域是否为灰色
  - (0,0) 是否处于合理的可通行区域
  - 红色 +X 方向是否与开始建图时机器人的前方一致

  如果地图严重重影、墙体错位或走廊断裂，不建议直接用于导航。

  ———

  ## 11. 查看完成后的清理

  在运行临时 TF 的终端按：

  Ctrl+C

  在运行地图服务器的终端按：

  Ctrl+C

  确认临时 TF 已停止：

  rosnode list | grep map_to_odom_view

  没有输出即表示已停止。

  正式启动定位导航前，必须停止临时发布的 map → odom，否则可能与定位节点发布的 TF 冲突。

  如果相关终端丢失，可以先检查：

  rosnode list | grep -E 'map_to_odom_view|map_server'

  再根据实际节点名称执行：

  rosnode kill /map_to_odom_view

  地图服务器通常带随机编号，例如：

  /map_server_1788184814652683737

  需要使用 rosnode list 显示的完整实际名称停止。
 
