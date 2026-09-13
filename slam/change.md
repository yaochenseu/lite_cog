# MID-360 ROS1 建图外参修改记录

## 修改内容

修改文件：`src/faster-lio/config/c16.yaml`

- 保留 `/rslidar_points`、`/imu/data` 和 `lidar_type: 4`，继续使用现有 ROS1 `PointCloud2` 建图入口。
- 将 `extrinsic_est_en` 从 `true` 改为 `false`，首次验证时固定使用配置外参，避免在线估计掩盖初始外参问题。
- 将外参平移从 `[0.075, 0.0, 0.023]` 改为 `[0.187, 0.0, 0.073]` 米。
- 将原来的绕 Z 轴 90 度矩阵改为与当前 `base_link -> rslidar` 静态 TF 一致的绕 Y 轴正向 18 度矩阵：

```text
[ 0.9510565, 0.0,  0.3090170
  0.0,       1.0,  0.0
 -0.3090170, 0.0,  0.9510565 ]
```

Faster-LIO 中该参数按以下方向使用：

```text
p_imu = R_lidar_to_imu * p_lidar + T_lidar_to_imu
```

## 修改原因

当前 MID-360 驱动 JSON 使用零外参，18 度安装外参只发布在 TF 树中；Faster-LIO 不读取该 TF，原 `c16.yaml` 又只包含 C16 的绕 Z 轴 90 度外参，导致 MID-360 安装俯仰没有进入建图点云变换。

## 影响范围

- 只影响通过 `mapping_c16.launch` 启动的后续 Faster-LIO 建图。
- 不修改 MID-360 驱动 JSON、`base_link -> rslidar` 静态 TF、HDL Localization 或导航配置。
- 不会改变已生成的 PCD/PGM/YAML；旧地图仍保留原坐标和倾斜。
- YAML 在 launch 启动时加载，本次修改不需要重新编译。

## 已知限制

- 此配置按 `/imu/data` 使用 `base_link` 轴和原点的当前软件约定设置。若真实 IMU 原点不同，平移仍需后续实测校准。
- Faster-LIO 首帧未经外参变换就加入内部 IVox 的代码问题尚未修改。
- MID-360 PointCloud2 的逐点时间戳被当前 C16 预处理器忽略的问题尚未修改。
- 在静态点云确认地面和天花板恢复水平前，不应直接进行运动建图或真实导航。
