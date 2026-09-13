cmake_minimum_required(VERSION 2.8.3)
project(football)

set(CUDA_USE_STATIC_CUDA_RUNTIME OFF)

set(CMAKE_BUILD_TYPE "Release")
#set(CMAKE_BUILD_TYPE "Debug")

set(CMAKE_CXX_FLAGS "-std=c++14 -pthread")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")

find_package(catkin REQUIRED COMPONENTS
    roscpp
    cv_bridge
    sensor_msgs
    message_generation
    image_transport
)
find_package(OpenCV 4.2.0 REQUIRED)

find_package(PkgConfig REQUIRED)
# glib
pkg_check_modules(GLIB REQUIRED glib-2.0)
# gstreamer
pkg_check_modules(GLIB REQUIRED gstreamer-1.0)
pkg_check_modules(GLIB REQUIRED gstreamer-app-1.0)

message("OpenCV_DIR is ${OpenCV_DIR}")
message("OpenCV_FOUND is ${OpenCV_FOUND}")
message("OpenCV_LIBS is ${OpenCV_LIBS}")
message("OpenCV_INCLUDE_DIRS is ${OpenCV_INCLUDE_DIRS}")

link_directories("/usr/local/lib")

add_message_files(
   FILES
   circle.msg
)

generate_messages(
   DEPENDENCIES
   std_msgs
)

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
    ${OpenCV_INCLUDE_DIRS}
    ${GSTREAMER_INCLUDE_DIRS}
    ${GSTAPP_INCLUDE_DIRS}
    ${GLIB_INCLUDE_DIRS}
)

catkin_package()

add_library(ball_detector
    src/BallDetector.cpp
)
add_dependencies(ball_detector ${catkin_EXPORTED_TARGETS})
target_link_libraries(ball_detector
    ${catkin_LIBRARIES}
    ${OpenCV_LIBS}
    ${GSTREAMER_LIBRARIES}
    ${GSTAPP_LIBRARIES}
    ${GLIB_LIBRARIES}
)

add_executable(detect_ball src/DetectBall.cpp)
add_dependencies(detect_ball ${catkin_EXPORTED_TARGETS})
target_link_libraries(detect_ball ${catkin_LIBRARIES} ball_detector)

add_executable(control_ball src/ControlBall.cpp)
add_dependencies(control_ball ${catkin_EXPORTED_TARGETS})
target_link_libraries(control_ball ${catkin_LIBRARIES})
