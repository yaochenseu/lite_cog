# Details

Date : 2024-07-31 23:12:39

Directory /media/zox/36c0d412-c5a3-4d73-8ece-b4e01cfb90e6/home/ysc/lite_cog/slam/src/faster-lio

Total : 65 files,  7198 codes, 1625 comments, 1352 blanks, all 10175 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [app/run_mapping_offline.cc](/app/run_mapping_offline.cc) | C++ | 71 | 7 | 21 | 99 |
| [app/run_mapping_online.cc](/app/run_mapping_online.cc) | C++ | 35 | 5 | 12 | 52 |
| [cmake/FindGlog.cmake](/cmake/FindGlog.cmake) | CMake | 192 | 0 | 18 | 210 |
| [cmake/packages.cmake](/cmake/packages.cmake) | CMake | 50 | 0 | 10 | 60 |
| [config/avia.yaml](/config/avia.yaml) | YAML | 40 | 1 | 8 | 49 |
| [config/c16.yaml](/config/c16.yaml) | YAML | 40 | 1 | 7 | 48 |
| [config/horizon.yaml](/config/horizon.yaml) | YAML | 37 | 1 | 6 | 44 |
| [config/ouster64.yaml](/config/ouster64.yaml) | YAML | 40 | 1 | 7 | 48 |
| [config/velodyne.yaml](/config/velodyne.yaml) | YAML | 41 | 1 | 7 | 49 |
| [config/velodyne_liosam.yaml](/config/velodyne_liosam.yaml) | YAML | 41 | 1 | 7 | 49 |
| [config/velodyne_ulhk.yaml](/config/velodyne_ulhk.yaml) | YAML | 41 | 1 | 8 | 50 |
| [config/velodyne_utbm.yaml](/config/velodyne_utbm.yaml) | YAML | 41 | 1 | 8 | 50 |
| [docker/.env](/docker/.env) | Properties | 2 | 5 | 4 | 11 |
| [docker/Dockerfile](/docker/Dockerfile) | Docker | 9 | 7 | 6 | 22 |
| [docker/docker-compose.yml](/docker/docker-compose.yml) | YAML | 21 | 2 | 5 | 28 |
| [docker/ros_entrypoint.sh](/docker/ros_entrypoint.sh) | Shell Script | 12 | 3 | 9 | 24 |
| [include/IKFoM_toolkit/esekfom/esekfom.hpp](/include/IKFoM_toolkit/esekfom/esekfom.hpp) | C++ | 1,541 | 211 | 150 | 1,902 |
| [include/IKFoM_toolkit/esekfom/util.hpp](/include/IKFoM_toolkit/esekfom/util.hpp) | C++ | 31 | 33 | 9 | 73 |
| [include/IKFoM_toolkit/mtk/build_manifold.hpp](/include/IKFoM_toolkit/mtk/build_manifold.hpp) | C++ | 100 | 101 | 20 | 221 |
| [include/IKFoM_toolkit/mtk/src/SubManifold.hpp](/include/IKFoM_toolkit/mtk/src/SubManifold.hpp) | C++ | 15 | 91 | 12 | 118 |
| [include/IKFoM_toolkit/mtk/src/mtkmath.hpp](/include/IKFoM_toolkit/mtk/src/mtkmath.hpp) | C++ | 145 | 107 | 37 | 289 |
| [include/IKFoM_toolkit/mtk/src/vectview.hpp](/include/IKFoM_toolkit/mtk/src/vectview.hpp) | C++ | 76 | 77 | 18 | 171 |
| [include/IKFoM_toolkit/mtk/startIdx.hpp](/include/IKFoM_toolkit/mtk/startIdx.hpp) | C++ | 143 | 123 | 34 | 300 |
| [include/IKFoM_toolkit/mtk/types/S2.hpp](/include/IKFoM_toolkit/mtk/types/S2.hpp) | C++ | 159 | 85 | 26 | 270 |
| [include/IKFoM_toolkit/mtk/types/SOn.hpp](/include/IKFoM_toolkit/mtk/types/SOn.hpp) | C++ | 119 | 129 | 40 | 288 |
| [include/IKFoM_toolkit/mtk/types/vect.hpp](/include/IKFoM_toolkit/mtk/types/vect.hpp) | C++ | 250 | 104 | 62 | 416 |
| [include/IKFoM_toolkit/mtk/types/wrapped_cv_mat.hpp](/include/IKFoM_toolkit/mtk/types/wrapped_cv_mat.hpp) | C++ | 41 | 39 | 16 | 96 |
| [include/common_lib.h](/include/common_lib.h) | C++ | 166 | 42 | 38 | 246 |
| [include/imu_processing.hpp](/include/imu_processing.hpp) | C++ | 246 | 16 | 60 | 322 |
| [include/ivox3d/eigen_types.h](/include/ivox3d/eigen_types.h) | C++ | 58 | 10 | 17 | 85 |
| [include/ivox3d/hilbert.hpp](/include/ivox3d/hilbert.hpp) | C++ | 550 | 167 | 114 | 831 |
| [include/ivox3d/ivox3d.h](/include/ivox3d/ivox3d.h) | C++ | 238 | 21 | 49 | 308 |
| [include/ivox3d/ivox3d_node.hpp](/include/ivox3d/ivox3d_node.hpp) | C++ | 328 | 4 | 80 | 412 |
| [include/laser_mapping.h](/include/laser_mapping.h) | C++ | 130 | 15 | 33 | 178 |
| [include/options.h](/include/options.h) | C++ | 13 | 5 | 7 | 25 |
| [include/pointcloud_preprocess.h](/include/pointcloud_preprocess.h) | C++ | 88 | 25 | 20 | 133 |
| [include/so3_math.h](/include/so3_math.h) | C++ | 76 | 4 | 14 | 94 |
| [include/use-ikfom.hpp](/include/use-ikfom.hpp) | C++ | 90 | 4 | 16 | 110 |
| [include/utils.h](/include/utils.h) | C++ | 84 | 14 | 17 | 115 |
| [launch/gdb_debug_example.launch](/launch/gdb_debug_example.launch) | XML | 15 | 3 | 5 | 23 |
| [launch/mapping_avia.launch](/launch/mapping_avia.launch) | XML | 15 | 1 | 6 | 22 |
| [launch/mapping_c16.launch](/launch/mapping_c16.launch) | XML | 15 | 1 | 6 | 22 |
| [launch/mapping_horizon.launch](/launch/mapping_horizon.launch) | XML | 15 | 1 | 5 | 21 |
| [launch/mapping_ouster64.launch](/launch/mapping_ouster64.launch) | XML | 15 | 1 | 6 | 22 |
| [launch/mapping_velodyne.launch](/launch/mapping_velodyne.launch) | XML | 15 | 1 | 5 | 21 |
| [launch/mapping_velodyne_liosam.launch](/launch/mapping_velodyne_liosam.launch) | XML | 15 | 1 | 5 | 21 |
| [launch/mapping_velodyne_ulhk.launch](/launch/mapping_velodyne_ulhk.launch) | XML | 15 | 1 | 5 | 21 |
| [launch/mapping_velodyne_utbm.launch](/launch/mapping_velodyne_utbm.launch) | XML | 15 | 1 | 5 | 21 |
| [log/list_2024-07-31_22-44-14/logger_all.log](/log/list_2024-07-31_22-44-14/logger_all.log) | Log | 19 | 0 | 1 | 20 |
| [msg/Pose6D.msg](/msg/Pose6D.msg) | ROS Interface | 6 | 1 | 0 | 7 |
| [package.xml](/package.xml) | XML | 36 | 0 | 9 | 45 |
| [result/plot_bar_time_by_step.py](/result/plot_bar_time_by_step.py) | Python | 47 | 2 | 8 | 57 |
| [result/plot_nn.py](/result/plot_nn.py) | Python | 23 | 1 | 6 | 30 |
| [result/plot_process_recall.py](/result/plot_process_recall.py) | Python | 39 | 2 | 12 | 53 |
| [result/plot_time.py](/result/plot_time.py) | Python | 34 | 7 | 7 | 48 |
| [result/plot_time_usage.py](/result/plot_time_usage.py) | Python | 82 | 34 | 20 | 136 |
| [result/rpe_odom.py](/result/rpe_odom.py) | Python | 56 | 5 | 14 | 75 |
| [rviz_cfg/loam_livox.rviz](/rviz_cfg/loam_livox.rviz) | YAML | 389 | 0 | 1 | 390 |
| [src/laser_mapping.cc](/src/laser_mapping.cc) | C++ | 695 | 51 | 125 | 871 |
| [src/options.cc](/src/options.cc) | C++ | 6 | 3 | 4 | 13 |
| [src/pointcloud_preprocess.cc](/src/pointcloud_preprocess.cc) | C++ | 182 | 3 | 40 | 225 |
| [src/utils.cc](/src/utils.cc) | C++ | 4 | 3 | 4 | 11 |
| [thirdparty/livox_ros_driver/msg/CustomMsg.msg](/thirdparty/livox_ros_driver/msg/CustomMsg.msg) | ROS Interface | 6 | 1 | 3 | 10 |
| [thirdparty/livox_ros_driver/msg/CustomPoint.msg](/thirdparty/livox_ros_driver/msg/CustomPoint.msg) | ROS Interface | 7 | 1 | 3 | 11 |
| [thirdparty/livox_ros_driver/package.xml](/thirdparty/livox_ros_driver/package.xml) | XML | 32 | 36 | 15 | 83 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)