
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>

#include <opencv2/core.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <memory>
#include <thread>
#include <math.h>

#include <football/circle.h>

#include "GStreamerWrapper.hpp"


class BallDetector{
public:
    BallDetector(ros::NodeHandle nh);
    void ImageCB(const sensor_msgs::ImageConstPtr &msgRGB);
    void DetectThread();
    void DetectBall(const cv::Mat &img);

    ros::NodeHandle nh_;
    ros::NodeHandle private_nh_;

    bool is_rtsp_ = false;

    std::string img_topic_;
    std::string box_topic_;

    ros::Subscriber image_sub_;

    std::shared_ptr<GStreamerWrapper> gstreamer_;
    std::thread detect_thread_;

    bool is_debug_ = false;

    int hsv_thresh_0_low_ = 0;
    int hsv_thresh_0_high_ = 0;
    int hsv_thresh_1_low_ = 0;
    int hsv_thresh_1_high_ = 0;
    int hsv_thresh_2_low_ = 0;
    int hsv_thresh_2_high_ = 0;

    int area_thresh_ = 0;
    double afa_thresh_ = 0;

    int frame_width_ = 0;
    int frame_height_ = 0;
    football::circle ball_circle_last_;
    ros::Publisher ball_circle_pub_;
};