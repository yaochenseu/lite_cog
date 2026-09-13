cmake_minimum_required(VERSION 3.0.2)
project(scan_map_navigation)
add_compile_options(-std=c++14 -O2)
find_package(catkin REQUIRED COMPONENTS roscpp rospy actionlib actionlib_msgs
  geometry_msgs nav_msgs sensor_msgs std_msgs std_srvs tf tf2_ros costmap_2d
  global_planner plan_env path_searching bspline_opt traj_utils cv_bridge visualization_msgs message_generation)
find_package(Eigen3 REQUIRED)
find_package(PCL REQUIRED)
set(SCAN_ROOT "/home/ysc/lite_cog/SCAN-Planner" CACHE PATH "Existing built SCAN workspace")
# Upstream exports a nonexistent libscan_planner. Use its generated messages and
# source manager explicitly; link only its real dependency libraries.
if(NOT EXISTS "${SCAN_ROOT}/devel/include/scan_planner/Bspline.h")
  message(FATAL_ERROR "Build the original SCAN-Planner workspace first")
endif()
add_action_files(FILES Navigate.action)
add_message_files(FILES VelocityCommand.msg NavigationControl.msg LocalTarget.msg LocalTrajectory.msg)
add_service_files(FILES CheckPoses.srv)
generate_messages(DEPENDENCIES actionlib_msgs geometry_msgs std_msgs)
catkin_package(CATKIN_DEPENDS message_runtime geometry_msgs actionlib_msgs)
include_directories(include ${catkin_INCLUDE_DIRS} ${EIGEN3_INCLUDE_DIRS} ${PCL_INCLUDE_DIRS}
  "${SCAN_ROOT}/devel/include" "${SCAN_ROOT}/src/planner/plan_manage/include")
add_executable(map_global_planner src/map_global_planner.cpp)
add_executable(map_scan_planner src/scan_planner_node.cpp src/scan_replan_fsm.cpp
  "${SCAN_ROOT}/src/planner/plan_manage/src/planner_manager.cpp")
add_executable(map_scan_controller src/closed_loop_controller.cpp)
foreach(target map_global_planner map_scan_planner map_scan_controller)
  target_link_libraries(${target} ${catkin_LIBRARIES})
  add_dependencies(${target} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
endforeach()
catkin_install_python(PROGRAMS scripts/navigator.py scripts/velocity_gate.py scripts/goto.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
