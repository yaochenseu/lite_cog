# Lite3 地图导航 + SCAN 滚动中间目标

独立 ROS1 工作空间。原 `nav`、`SCAN-Planner`、雷达驱动、transfer 和地图未修改。

## 当前数据流

```text
PCD + MID360 + IMU → 原 NDT → map→odom
PGM/YAML → Dijkstra → 全局路径（保留在 map）
                             ↓
                 有顺序的滚动前视中间点
                             ↓ 同一 TF 时刻的定位校正
                       odom 局部目标
                             ↓
MID360 + leg_odom2 → SCAN 局部地图、规划和闭环控制
                             ↓ 直接输出带任务标识的速度
                 独立限速、健康与超时保护 → cmd_vel → ros2qnx
```

目标管理器不订阅 raw_cmd，不转发速度，不同步调用碰撞检查服务。
正常换点、普通定位修正不清空 SCAN。中间点提前切换，不要求逐点停稳或对齐朝向。
真正的终点在 map 中判断到达；固定朝向由 SCAN 控制器对齐，局部规划器检查旋转足迹。

## 使用

关闭旧导航及独立 SCAN 窗口，保留 transfer；不要同时运行两套速度控制。
雷达没有数据时，单独终端启动：

```bash
bash /home/ysc/lite_cog/system/scripts/lidar/start_livox.sh
```

**本次修改了 C++ 和消息定义，必须编译并完整重启本套导航，不能只重启 goto。**

```bash
cd /home/ysc/lite_cog/scan_map_nav
./build.sh
./start_nav.sh
```

默认使用 system/map/lite3.pcd、lite3.yaml、waypoints.yaml。
零初值对应建图起点和起始朝向，不是全局自动定位。先在 RViz 确认定位正确。
不在固定起点时，用 2D Pose Estimate 或启动参数提供初值：

```bash
./start_nav.sh init_x:=0.0 init_y:=0.0 init_yaw:=0.0
```

另一个终端：

```bash
cd /home/ysc/lite_cog/scan_map_nav
./goto hall
./goto room
./goto door
./goto hall --any-yaw
./goto --cancel
```

无需 arm/解锁。启动无目标时保持停止。使用本目录 ./goto，不要混用旧 PATH 的 goto。
新目标替换旧目标；故障终止后恢复输入再发新目标，旧任务不自动续走。
首测只选空旷短距离目标，保留遥控急停。结束时先 ./goto --cancel，再关闭导航。

## 行为与参数

参数文件：src/scan_map_navigation/config/rolling.yaml。

- 前视距离 0.9 m，正常目标更新间隔至少 0.3 s，沿路径移动约 0.18 m 才更新；每秒补发防止丢失，SCAN 忽略重复点。
- 同一目标受定位校正影响超过 0.08 m 时更新其 odom 坐标。
- 前视目标不能跳过大转角；选点时做静态地图视线检查，避免隔墙取点。不是原来逐条速度的静态机身检查。
- 单次附近定位变换突变超过 0.8 m 或 0.5 rad，停车报错，请检查 RViz 后重发目标。普通修正不进入“等待稳定—清空—重建”的循环。
- 无可用前视点、偏离路径或 15 秒无进展时，最多请求 2 次全局重新规划。只有任务边界或这类异常重规划调用 reset。
- XY 容差 0.15 m，最终朝向容差 0.12 rad。
- 前进/后退/横移/偏航上限仍为 0.35/0.18/0.25 m/s、0.8 rad/s；最终对齐上限 0.4 rad/s。

SCAN 使用新增的 mode 4，单个中间目标接续局部重规划；不再把整条 Dijkstra 路径转换成全局多项式。
机器人双圆柱尺寸仍是半径 0.35 m、中心偏置 ±0.18 m，没有缩小。
当前未启用原手动单目标模式的死路后退恢复。

## 指令与故障隔离

- navigator 发布短期任务许可 /scan_map_nav/control，而不是速度；有效期 0.5 秒。
- 控制器直接发布 /scan_map_nav/desired_cmd；速度有效期 0.25 秒。
- 目标、轨迹、速度携带 task_id 和 epoch。取消、替换目标或输入故障不能把旧轨迹当作新任务执行。
- gate 通过 /scan_map_nav/execution_allowed 反馈放行状态；未放行或反馈超时，控制器输出零并冻结轨迹时钟。
- SCAN 自身避障与紧急停车保留。取消、健康故障、明显定位跳变仍停止。
- 传感器及规划心跳超时仍为 0.7 秒；NDT 收敛、inlier ≥ 0.5、matching_error ≤ 0.3 的检查未放宽。
- 已移除正常启动中的 static_check 参数和 route_recovery 等待逻辑。legacy_navigator.py、recovery.yaml 仅保留为历史参考，不启动。

## 查看状态

```bash
cd /home/ysc/lite_cog/scan_map_nav
source env.sh
rostopic echo /scan_map_nav/task_state
rostopic echo /scan_map_nav/gate_state
rostopic echo /scan_map_nav/local_target
rostopic info /cmd_vel
```

/cmd_vel 应只有 /scan_velocity_gate 发布，/cmd_vel_corrected 不应有竞争发布者。
RViz 中橙色球是当前 odom 中间目标；全局路径显示在 map 中。末次目标标记约两秒后消失。
任务状态：PLANNING、TRACKING、ALIGNING、REPLANNING、SUCCEEDED、CANCELLED、ABORTED。
gate 的 IDLE 表示无活动任务且输入正常，READY 表示当前指令可放行；Controller command expired、Task lease invalid/expired 会明确说明超时原因。

## 边界及测试

```bash
cd /home/ysc/lite_cog/scan_map_nav
./test.sh
```

测试使用私有 localhost ROS master 和 /test/cmd_vel，不启动 ros2qnx。
集成测试中定位修正只改变 map→odom，不改变连续的腿式里程计。
历史等待恢复单测仅用于保留旧实现对照，不代表当前导航仍使用该逻辑。

这不是实机验收：真实雷达噪声、NDT 延迟、机身动力学和算力负载仍需实测。
本次没有改上游 NDT 的时间戳合成，也没有改 SCAN 的点云/雷达位姿配对。
全局规划仍只有 static+inflation；请求重规划不保证能绕开只存在于实时雷达中的封路障碍。
选点视线检查不是全路径足迹证明，实际避障仍依赖 SCAN 的实时局部地图。
软件停车不能替代底盘硬件看门狗和遥控急停。结果见 TEST_RESULTS.md。
