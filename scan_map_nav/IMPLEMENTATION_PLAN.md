# 历史：运行时地图与自适应前视实现审计

2026-09-16：按用户要求回退到静态地图 Dijkstra + 0.9 m 滚动目标 + SCAN。
本文件以下内容只描述回退前实现，不能作为当前启用功能或当前验收结论。
实时地图源码与实验辅助模块保留但不接入正常导航；当前操作见 README.md，验证见 TEST_RESULTS.md。

任务依据：用户附件 39da9c00-4cdc-4fa3-a3df-62fbf3787674/pasted-text-1.txt。
此清单是实施与验证记录，不缩小附件要求。未勾选项不得宣称完成。

- [x] 保存的 PGM/PCD 与定位组件未改；记录前后哈希。
- [x] 点云按观测时间变换；过滤无效、机身、地面，健康/TF 不可靠时不更新。
- [x] 新障碍写入运行时地图；旧障碍仅凭连续、多高度空闲射线证据清除。
- [x] 未观察、遮挡、漏扫、过期、断流不产生空闲；明确运行时覆盖生命周期与重启语义。
- [x] 占据修正后统一重算膨胀；规划、路径检查、选点共用同版本地图。
- [x] 正常 0.9 m 目标、独立约 2 m 路径足迹检查；持续阻塞确认不打断有效绕行。
- [x] 受阻按 1.3/1.6/2.0 m 有界尝试；目标足迹安全、拓扑约束、不跳支路。
- [x] 有证据的新增障碍可以位于目标直线中间；完整 SCAN 候选碰撞检查不删减。
- [x] 受控目标替换可解除局部恢复冻结；同任务新 generation，旧轨迹不得重放。
- [x] 每档/总尝试预算，正常转向/绕行进展，有限偏离，稳定后逐步恢复 0.9 m。
- [x] 失败后后台串行全局规划，验证候选后接入；安全旧轨迹继续，已急停保持零。
- [x] 最终目标/task 保持；普通换路不 reset；无安全路线停止并报告阻塞。
- [x] 许可续期/恢复、取消、输入故障、定位质量、尺寸、限速及急停保护回归。
- [x] 单测、真实 Dijkstra/SCAN 私有 ROS 集成、地图增删/遮挡/断流/膨胀、后台换路测试。
- [x] 文档、参数、RViz、重启/构建命令与实际实现一致；逐项记录证据和未验收边界。

验证只使用私有 localhost master 与 /test/cmd_vel，不控制实机。实机动力学与现场定位效果不由隔离测试代替。

## 后续实机故障修正：延迟 TF 导致 Stale map

用户首次实测暴露了原同步 TF 仿真的覆盖缺口：实时点云到达时 NDT 尚未发布该时间戳的 TF，旧 50 ms 等待策略丢帧。已改为 8 帧／16 MiB 有界缓存、10 ms 非阻塞重试，处理最新可变换帧；保留原 0.7 秒总时效、真实源时间戳和所有安全阈值。

新增延迟回归先在旧二进制上复现失败，再在新版本通过：180/300 ms 延迟下地图持续新鲜且实际 Dijkstra 可用，950 ms 延迟拒绝过期队列，恢复不重放旧积压。完整新轮次 `test.sh` 退出 0，记录位于 TEST_RESULTS.md 的“当前”章节。下列基础版本证据保留，但不再单独用来证明异步 TF 兼容性。实机影子对照因用户已关闭导航、缺少 /map 未完成；未擅自重启实机。

## 逐项源码与测试证据

以下路径均相对于本目录；最终运行结果还须与 TEST_RESULTS.md 对照。

| 附件要求 | 实现位置与可验证证据 |
| --- | --- |
| 二：正常方法、坐标校正、不逐点停车 | `scripts/navigator.py` 的同时间戳 snapshot、map 路线和 odom 目标；`rolling_route.py` 的有序进度；`rollingTargetCallback` 保留执行中轨迹。`test_navigation_checks.py`、常规隔离导航验证实际 Dijkstra/SCAN、普通定位校正及无全局 reset。脚本均在 `src/scan_map_navigation/` 下。 |
| 三：新增、可靠清除、未观察保持 | `src/runtime_map.cpp` 使用云时间戳查询各 TF，验证 NDT/字段/范围、过滤机身和地面；`include/scan_map_navigation/evidence_grid.h` 每帧占据优先、三高度带连续证据、端点保护、无超时转空闲。C++ 测试覆盖重复/缺帧/遮挡/地面/未知；`isolated_runtime_map.py` 使用首表面回波验证实际增删、缺失 TF、断流、NDT 拒绝。 |
| 三：膨胀、同版本地图、生命周期 | `map_global_planner.cpp` 从修正占据重建完整原生代价，PlanningGrid 同消息携带占据/拓扑/代价/版本，Dijkstra 与 navigator 共用。实际箱子移走测试确认膨胀消失、通路开放。空闲覆盖 5 秒失效回先验，占据不按时消失，重启只读原先验；README 与参数明确，不写 PGM/PCD。 |
| 四：2 m 走廊、确认、紧急风险优先 | `planning_grid.py` 的 route_blocked 使用双圆机身；BlockageConfirmation 需 1 秒且不同版本。navigator 仅在停滞/失败时升级，有平移或转向进展则继续；SCAN beginLocalRecovery 先发布停车状态。单测区分 0.9 m 目标与 2 m 检查、覆盖路径宽度与多版本确认。 |
| 五：临时阶梯、合法选点、有限恢复 | AdaptiveLookahead 与 candidate：0.9/1.3/1.6/2.0 m，足迹和先验拓扑约束，允许新增箱子在中间；每档 10 秒、总计 30 秒、2 m 偏离边界、1.5 秒稳定后逐档恢复。单测验证预算/拐角/未知/恢复，实际 SCAN 专项验证三档先于全局、受控解冻、新 generation、同任务恢复。不是永久稀疏模式。 |
| 五：完整轨迹碰撞检查 | `scan_replan_fsm.cpp::validateLocalTrajectory` 验证初始转向和整个候选（含终点）；保留原机身参数。接入层未退回上游仅检查前 2/3 的行为。gate/controller 的 generation 校验禁止旧轨迹重新放行。 |
| 六：后台串行、验证后换路、保持任务 | AsyncPlan 不具备执行提交权限；navigator 单 pending 请求，校验 task、最新代价与移动接入后替换。`test_async_execution.py` 运行真实 execute 循环和延迟 worker，验证等待时继续 TRACK、不 reset、取消拒绝迟到结果；实际持续局部失败验证最多两次全局恢复后零速度阻塞。 |
| 一、二、七：保护不退化 | 常规隔离回归覆盖取消、输入故障、独立续期、软超时恢复和硬超时撤销、非零报告速度下立即重试；`test_gate.py` 验证阈值/限速/代号拒绝。源码与 git diff 确认尺寸、速度、NDT 门槛、断流门槛不放宽；地图哈希见下。 |

## 最终运行证据（2026-09-16）

- 最新 C++ 增量构建通过，含地面端点不标记与整格膨胀；Python 110 项通过，C++ evidence_grid_test 通过。
- 地图/膨胀/实际 Dijkstra 增删专项：`/tmp/scan_runtime_map_test_7gcccsxp/`。
- 常规导航与许可/取消/故障回归：`/tmp/scan_map_nav_test_ksopfz1x/`。
- 实际 SCAN 加长目标协议与三档后全局回退：`/tmp/scan_map_nav_test_1h4ly8q5/`。
- 首轮专项暴露同循环两次状态发布会丢失 EXTENDING_TARGET，已改为每循环一次发布；上述新轮次已验证提示及实际协议。
- 新增箱子，仅 SCAN 临时加长绕行并完成：`/tmp/scan_map_nav_test_rje8csit/`；只用初始全局路线，机身采样净距 0.083 m。
- 新增箱子、注入局部失败后实际 Dijkstra 重规划并完成：`/tmp/scan_map_nav_test_l8lc03w9/`；箱子始终保留，机身采样净距 0.026 m。两个场景均要求净距 >= 0，未缩小机身。
- 完整 `./test.sh` 已正常退出 0，所有上述专项在同一轮依次通过；只使用隔离 master 与测试速度话题。源码审计与测试证明附件的代码实现和隔离验证要求已完成，不宣称实机已验收。
- `git diff --check -- scan_map_nav`、启动/构建/测试脚本 bash 语法检查通过。真实 navigation.launch 已在本轮各隔离场景加载；RViz 的原图、运行时占据和膨胀代价话题与发布代码一致。

修改前后均检查的文件 SHA-256：

```text
f3262ca19afc8b9b54f8078fd0ddce8a69332748869ebd8d8d9525aca015869b  system/map/lite3.pgm
284ab2f5ca75a48148a95627408b9ce2e648a95faa788bd6010843fe19ac4816  system/map/lite3.pcd
4194d1479a68b97a23f94c33dcd265cccaa59f3dad86d5403f4bacfb1a8b9228  system/map/lite3.yaml
064ccf079a3fd2bffed8e99198a2896bc4f211263fbc7c6dfd298a67df30ef9a  system/map/waypoints.yaml
```
