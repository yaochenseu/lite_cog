# Install script for directory: /home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/opt/ros/noetic")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "None")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lslidar_msgs/msg" TYPE FILE FILES
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/msg/LslidarPacket.msg"
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/msg/LslidarPoint.msg"
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/msg/LslidarScan.msg"
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/msg/LslidarC16Sweep.msg"
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/msg/LslidarC32Sweep.msg"
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/msg/LslidarScanUnified.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lslidar_msgs/srv" TYPE FILE FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/srv/lslidar_control.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lslidar_msgs/cmake" TYPE FILE FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/catkin_generated/installspace/lslidar_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/devel/include/lslidar_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/devel/share/roseus/ros/lslidar_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/devel/share/common-lisp/ros/lslidar_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/devel/share/gennodejs/ros/lslidar_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/devel/lib/python3/dist-packages/lslidar_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/devel/lib/python3/dist-packages/lslidar_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/catkin_generated/installspace/lslidar_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lslidar_msgs/cmake" TYPE FILE FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/catkin_generated/installspace/lslidar_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lslidar_msgs/cmake" TYPE FILE FILES
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/catkin_generated/installspace/lslidar_msgsConfig.cmake"
    "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/catkin_generated/installspace/lslidar_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/lslidar_msgs" TYPE FILE FILES "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/ls/work/fuhong/rospackage/new_driver/CX_4.0_ROS/ROS1/src/LSLIDAR_CX_V4.2.0_220823_ROS/lslidar_ros/lslidar_msgs/.obj-x86_64-linux-gnu/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
