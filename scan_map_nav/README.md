# Lite3 静态全局地图 + SCAN 滚动目标导航

当前使用静态地图 Dijkstra + 2.0 m 滚动目标 + SCAN 局部避障，不启用实时全局地图更新。
保留 SCAN 急停恢复和定位超时的有限自动重试；任务许可超时保护默认关闭，可通过启动参数开启。不需要 arm/解锁。
原 nav、SCAN-Planner、MID360 驱动、transfer、PGM/PCD 和航点文件未修改。

## 当前数据流

```text
PGM/YAML → StaticLayer + InflationLayer → Dijkstra → map 全局路径
                                                       ↓
                                                2.0 m 滚动目标
PCD + MID360 + IMU → 原 NDT → map→odom → 同时刻坐标校正
                                                       ↓
                                               odom 中间目标
MID360 + leg_odom2 → SCAN 局部地图、规划、闭环控制 → 速度门控 → ros2qnx
```

不再启动 scan_runtime_map，不依赖 runtime_grid / planning_grid，不要求静态地图每 0.7 秒更新。
雷达、IMU、里程计、定位、规划器心跳及动态 TF 的时效保护仍保留。

全局膨胀半径最新按用户要求从 0.10 m 改为 0.30 m（config/global.yaml），cost_scaling_factor 仍为 5.0。
这是从障碍格向外的总半径，不是机身外额外 30 cm。没有缩小 footprint 或 SCAN 的双圆柱尺寸，也没有取消局部碰撞检查。
相比 0.10 m，全局路径会受更大范围的障碍代价影响；不保证狭窄通道能通过，仍需 SCAN 检查实际机身碰撞。
此项只改配置，无需编译；先取消任务并关闭导航，再重新启动后生效，不在线修改正在执行的路线。

## 使用

先关闭其他导航及独立 SCAN，保留 transfer。不要同时运行两套速度控制。
MID360 没有数据时，在独立终端启动：

```bash
bash /home/ysc/lite_cog/system/scripts/lidar/start_livox.sh
```

更新代码后编译并完整重启本套导航，不能只重新运行 goto：

```bash
cd /home/ysc/lite_cog/scan_map_nav
./build.sh
./start_nav.sh
```

任务许可超时保护默认关闭。要启用原来的 0.3 秒计算进展检查、0.5 秒许可时效检查及超时停车恢复，先取消任务并退出旧导航，再启动：

```bash
./start_nav.sh task_lease_watchdog:=true
```

恢复默认关闭使用 `./start_nav.sh`（或显式 `task_lease_watchdog:=false`）。这是**启动开关**，同时设置导航管理器、速度门控和控制器；不支持运行中仅用 `rosparam set` 切换。
关闭后，导航管理程序卡顿时可能继续执行已有的局部目标，不再靠任务许可过期停车。取消/STOP、任务身份与轨迹代次校验、传感器/定位/规划心跳、速度指令时效和碰撞检查仍保留。请保留遥控急停；本次包含 C++ 控制器修改，更新后需要编译。

默认读取 system/map/lite3.pcd、lite3.yaml、waypoints.yaml。
零初值对应建图起点和起始朝向，不是全局自动定位；先在 RViz 确认定位正确。
不在固定起点时，使用 2D Pose Estimate 或明确初值：

```bash
./start_nav.sh init_x:=0.0 init_y:=0.0 init_yaw:=0.0
```

另一个终端：

```bash
cd /home/ysc/lite_cog/scan_map_nav
./goto hall
./goto room
./goto door
./goto arm
./goto hall --any-yaw
./goto --cancel
```

arm 是已有航点名称，不是解锁操作。启动无目标不运动；新目标替换旧目标。
首次测试选择空旷短距离目标，保留遥控急停。结束先 ./goto --cancel，再关闭导航。

## 滚动选点与恢复

- 正常前视 2.0 m，沿路径顺序推进，不跳到交叉路径或平行回程分支；转角或临近终点时可能更短。
- 转角切弯上限 0.12 m，选点中心连线不能穿过静态地图中的墙或未知区域。
- 管理循环 20 Hz；相对上次实际下发的引导点，地图位置变化达到 0.08 m 才更新，最小发布间隔仍为 0.05 秒。取消定时补发及接近旧点时 0.03 m 即更新的例外；没有明显变化就保持 SCAN 当前目标，不因经过 0.5 秒重新下发。
- 定位校正使该引导点的 odom 坐标相对上次下发变换偏移达到 0.08 m 时更新（包含平移及旋转的影响）。小幅真实变化相对上次下发累积，不逐帧重置比较基准；普通校正、正常换点不 reset。
- 首次目标、最终目标标记变化、局部失败/任务许可恢复或新全局路线所需的重新下发仍保留；取消的是正常跟踪中的无条件补发，不是故障后的重试。任务许可和状态心跳不受影响。RViz 引导点持续显示，任务结束或取消时删除，无需靠补发规划命令维持显示。
- 不使用永久稀疏点，也不再使用 1.3/1.6/2.0 m 自适应加长、2 m 走廊阻塞确认或实时地图后台换路。
- 连续 3 轮 SCAN 局部恢复耗尽后，从当前引导点开始，每次沿原路径前移 0.5 m；第三轮就尝试第一次前移，此后每失败一轮再前移一次，不是每一档重新等三轮。
- 正常 2.0 m 引导距离在直路受阻时依次尝试约 2.5、3.0、3.5、4.0、4.5、5.0 m。5 m 是沿路径前方距离上限，不是额外前移 5 m；本轮开始加长时固定其路径弧长上限，避免定位微调使上限不停前移。SCAN 自身 1.5 m 局部规划窗口不变，它分段朝较远目标规划。
- 实际动起来、引导点到终点、达到 5 m 上限，任一满足就停止本轮加长。末步不足 0.5 m 时截到终点或上限，不越界、不重复前移到同一点。穿静态墙/未知区域或切弯超限的候选点仍跳过，不关闭碰撞检查；因此不保证每条弯路都能实际下发 5 m 远的点。
- “动起来”要求 SCAN 处于 TRACKING 且连续 odom 中机身相对上次失败位置的平移距离达到 0.2 m；不是累计走过的路程，目前仍不区分前进、后退或横移。单次 TRACKING、原地转向、NDT 坐标校正不算成功。成功后清零失败计数，但保持已有效的远引导点，直到正常 2 m 滚动引导追上，避免立即缩回。再次连续三轮失败才重新开始加长。
- 到终点/5 m 或无合法加长点仍失败时，停止加长，按原节奏对最后有效点局部重试，不自动全局重规划；保留 300 秒总任务期限、取消及输入故障停车。
- `EXTENDING_TARGET +1.0m` 表示本轮相对初始引导点累计前移 1 m，不是单次前移 1 m。参数位于 config/rolling.yaml：guide_extension_failures=3、guide_extension_step=0.5、guide_extension_max_ahead=5.0、guide_extension_motion=0.2。
- 路线偏离超过 0.8 m、无法沿静态路线选点时，停车并有限全局重规划（最多 2 次）。
- 局部恢复耗尽、行进中 15 秒无运动进展，不再触发全局重规划；保持原路线和目标，停车间隔重试 SCAN。
- 全局重规划重新使用静态地图，不会看到新出现的箱子，也不会自动清除旧地图障碍。
- XY 到达容差 0.15 m；需要终点朝向时，朝向容差 0.12 rad，旋转也接受局部碰撞检查。

```text
SCAN 急停 → 零速度，保留目标与 map 路线
         → 暂停滚动切点，SCAN 从实测位置/速度重试
         → 新轨迹通过完整碰撞检查：继续同一任务
         → 局部恢复耗尽：BLOCKED_WAIT，保持停车 0.2 秒
         → 前两次 LOCAL_RETRY；第三次起每失败一轮沿路径前移 0.5 m
         → 仅 reset 局部规划/控制器，用所选引导点生成并复检新轨迹
         → 实际平移距离达到 0.2 m：停止加长，保持有效点，恢复正常跟踪
         → 到终点/5 m 仍失败：停车并间隔重试最后有效点，不因此重算全局路径
```

没有额外等待机身停稳的步骤，规划使用当前实测速度。
局部重试间隔 0.1 秒，最多 20 次或 3 秒；目标管理器另有 4 秒恢复上限。
以上是每轮的快速恢复预算；“3 次失败”按完整恢复轮次计，不是每次优化器内部迭代。
本轮耗尽后的轮间等待由 rolling.yaml 的 local_retry_wait 控制，默认 0.2 秒。
等待中持续发布 STOP，原 map 路线、最终目标及 task_id/epoch 不变；只提升局部 generation，旧轨迹不能复用。
再次尝试使用当前定位变换换算原引导点或本次前移点；必须生成并检查通过新轨迹才能运动。
整个任务仍受原 300 秒总期限约束，不因局部重试延长；取消、目标替换、输入故障仍打断等待，定位跳变使用下述多帧确认。
NDT 过期单独走下一节的有限定位恢复流程。任务许可超时保护由上述开关决定；机身尺寸、限速与碰撞检查不变，加快给点不保证消除其他原因的停车。

## 定位超时重试

- NDT `/status` 的源时间戳和接收时效从 0.7 秒放宽到 1.2 秒；导航 TF 时效和全局代价地图的 TF 容差同步为 1.2 秒。其余传感器与规划心跳仍为 0.7 秒。
- `Stale ndt` 或定位 TF 暂时不可用/过期：立即停车、清空旧局部轨迹，保留用户最终目标，显示 `LOCALIZATION_RECOVERY 1/3`。
- 每次最多等 3 秒，最多 3 次，整个 goto 任务累计计数；等到故障后产生的有效新 NDT 状态和新 TF 后即可提前恢复，不固定等待满 3 秒。
- 恢复后从当前位置重新生成全局路线及 SCAN 轨迹，以新的内部 task_id 和门控当前有效的 epoch 执行同一个 action 目标；不会复用失效的旧速度或旧轨迹，也不会重启 NDT 节点。
- 连续无定位时最多等待约 9 秒（另有 reset 等处理时间）；任务总期限仍为 300 秒，不因重试延长。取消、定位质量差、经多帧确认的持续跳变、其他输入故障仍终止任务。重试耗尽后保持停车，需重新发送目标。

仅调整这些定位启动参数无需编译，完整重启导航生效；本次任务许可开关涉及 C++，更新代码仍需编译。定位默认参数等价于：

```bash
./start_nav.sh localization_timeout:=1.2 localization_retries:=3 localization_retry_wait:=3.0
```

这增加延迟容忍和自动恢复，不提高 NDT 本身的计算速度；放宽时效也意味着可能使用更旧的定位结果，需现场低速短距离验收。

## 定位跳变多帧确认

- 原幅度阈值不变：坐标校正位移超过 0.8 m 或偏航变化超过 0.5 rad。首次超限进入 `LOCALIZATION_JUMP_HOLD`，立即 STOP、清空旧局部轨迹，保留最终目标和全局路线；不使用可疑定位更新引导点。
- 连续 5 个不同时间戳的定位 TF 采样异常，且这段异常至少持续 0.3 秒，才终止任务。重复读取同一帧、乱序旧帧不累计；确认期间始终与最后正常坐标及其附近探测点比较，不把第一次跳变当作新基准。
- 连续 3 个新采样回到正常范围，且持续至少 0.15 秒，才解除观察。用恢复后的坐标下发引导点，要求新的 SCAN 轨迹通过检查后恢复；不会重放旧轨迹或重新计算整条全局路线。
- 反复好坏、2 秒仍未稳定也终止并保持停车；取消、传感器故障、NDT 质量差、TF 超时和任务期限仍有优先权。TF/NDT 断流继续进入原有有限定位超时恢复，不能通过重试重置掉跳变前基准。
- 正常跟踪、局部重试等待和定位超时恢复均使用同一确认逻辑。日志记录首次异常的位移/角度/TF 时间戳，以及确认终止时的计数和幅度。
- 参数在 config/rolling.yaml：jump_confirm_frames=5、jump_confirm_time=0.3、jump_recover_frames=3、jump_recover_time=0.15、jump_hold_timeout=2.0。更新代码/配置后完整重启导航，无需重新编译。

## 保留的保护

- 任务意图仍由独立线程每 0.05 秒发布，保留最后一次计算时间戳；默认不根据任务许可年龄停车，仍校验任务身份、模式和无效/未来时间戳。
- **仅开启 task_lease_watchdog 时**：计算超过 0.3 秒未推进则停止续期；门控与控制器同时检查 0.5 秒许可时效。短暂失效立即停车、保留任务，恢复前必须完成局部规划器与控制器 reset、ACK 和新 generation 确认。
- **仅开启时**：许可恢复窗口 2 秒内始终停车；持续失联撤销任务，延迟旧指令不得继续运动。
- 非定位传感器和规划心跳超时仍为 0.7 秒；NDT 时效为 1.2 秒，仍要求收敛、inlier ≥ 0.5、matching_error ≤ 0.3。
- 同时间戳查询 map/base_link 与 odom/base_link；校正跳变先停车观察，多帧确认持续异常才终止，见上一节。
- 前进/后退/横移上限 0.35/0.18/0.25 m/s，偏航上限 0.8 rad/s，终点对齐上限 0.4 rad/s。
- 双圆柱半径 0.35 m、中心偏置 ±0.18 m；SCAN 局部规划范围 1.5 m，尺寸和完整候选碰撞检查未缩减。
- navigator 不处理速度、不逐条调用静态足迹审批；静态检查服务仅供诊断。
- 非定位时效类输入故障后需重新发送目标；局部避障、短暂许可及上述有限定位超时恢复不要求手动重发。

## 查看状态

```bash
cd /home/ysc/lite_cog/scan_map_nav
source env.sh
rostopic echo /scan_map_nav/task_state
rostopic echo /scan_map_nav/gate_state
rostopic echo /scan_map_nav/planner_state
rostopic echo /scan_map_nav/last_fault
rostopic info /cmd_vel
```

/cmd_vel 应只有 /scan_velocity_gate 发布，/cmd_vel_corrected 不应有竞争发布者。
RViz 显示静态地图、静态膨胀代价、map 全局路线及橙色滚动目标，不再显示实时占据层。
TRACKING 不保证速度已放行，实际情况查看 gate_state / planner_state。

## 测试与回退记录

```bash
cd /home/ysc/lite_cog/scan_map_nav
./test.sh
```

测试使用独立 localhost ROS master，仅输出 /test/cmd_vel，不启动 ros2qnx。
集成测试只发布一次故意使用旧时间戳的静态地图，且不启动 runtime_grid / planning_grid 发布者。
同时验证 Dijkstra 绕墙、SCAN 跟踪、终点朝向、定位校正、局部恢复、许可恢复、取消及输入故障。
局部恢复专项持续拒绝候选超过 15 秒并经历多轮预算，验证只有一条全局路线、始终停车；解除拒绝后同任务到达，并检查等待期间取消/断流/替换目标。
引导点专项验证未到旧点就更新、第三轮失败后每次前移 0.5 m、5 m/终点截断、实际移动后停止加长且不缩回、全程保留同一全局路径和任务、解除拒绝后到达。
另含定位专项：0.9 秒延迟、NDT/TF 断流恢复、取消、质量故障、定位跳变及三次重试耗尽。
新增 jump_confirmation 专项覆盖短暂跳变后同任务恢复、持续跳变终止、观察期间取消与 NDT 质量故障。此前常规长距离绕墙回归曾被局部碰撞检查拦停；最新 0.30 m 与多帧确认版本的实际验证范围见 TEST_RESULTS.md，不能用协议测试代替真实避障验收。
test_hooks 仅在显式启用且输出为 /test/cmd_vel 时注册，正常启动不提供。

回退前代码备份：
/home/ysc/lite_cog/scan_nav_rollback_backup.jCo4nG/scan_map_nav_before_rollback.tar.gz

本次定位超时重试修改前备份：
/home/ysc/lite_cog/scan_ndt_retry_backup.63rtaV/scan_map_nav_before_ndt_retry.tar.gz

局部失败仅局部重试修改前备份：
/home/ysc/lite_cog/scan_local_retry_backup.mxGV5R/scan_map_nav_before_local_retry.tar.gz

加快引导点与五档加长前备份：
/home/ysc/lite_cog/scan_guide_tuning_backup.2iyKsD/scan_map_nav_before_guide_tuning.tar.gz

2 m 引导点与更短更新间隔修改前备份：
/home/ysc/lite_cog/scan_2m_guide_backup.p9j5S6/scan_map_nav_before_2m_guide.tar.gz

0.5 m 递增加长到 5 m 修改前备份（包含默认关闭任务许可保护的版本）：
/home/ysc/lite_cog/scan_guide_halfmetre_backup.kLLP6E/scan_map_nav_before_halfmetre_guide.tar.gz

runtime_map.cpp、PlanningGrid、planning_grid.py、async_plan.py 及其历史测试保留供对照，
但当前导航不启动、不导入这套实时地图/自适应流程。historical_async_execution.py 只适用于回退前代码，
不计入当前回归；保留的纯逻辑模块测试也不代表当前启用了这些功能。
旧目标替换协议字段保持兼容，当前目标管理器不发送自适应 recovery_id。
IMPLEMENTATION_PLAN.md 的实时地图清单是历史记录，不是当前启用功能。

这次回退消除了实时规划地图时效这一依赖，不保证所有停车问题消失。
新的障碍仍由 SCAN 局部绕行；全局路径不适应环境增删，无法绕过时应保持停车。
隔离测试不代替真实 MID360/NDT 延迟、机身动力学和现场导航验收。结果见 TEST_RESULTS.md。
