
#include <ros/ros.h>

#include <string>

#include "BallDetector.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "detect_ball");
    ros::NodeHandle nh;
    BallDetector ball_detector(nh);
    ros::spin();
    return 0;
}
