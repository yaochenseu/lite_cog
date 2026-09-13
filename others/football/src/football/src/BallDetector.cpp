
#include "BallDetector.h"
#include "BallState.h"

BallDetector::BallDetector(ros::NodeHandle nh) 
: nh_(nh), private_nh_("~")
{
    private_nh_.getParam("is_rtsp", is_rtsp_);
    ROS_INFO("is_rtsp_: [%d]", is_rtsp_);

    private_nh_.getParam("img_topic", img_topic_);
    ROS_INFO("img_topic_: [%s]", img_topic_.c_str());
    private_nh_.getParam("box_topic", box_topic_);
    ROS_INFO("box_topic_: [%s]", box_topic_.c_str());

    private_nh_.getParam("is_debug", is_debug_);
    ROS_INFO("is_debug: [%d]", is_debug_);

    private_nh_.getParam("hsv_thresh_0_low", hsv_thresh_0_low_);
    ROS_INFO("hsv_thresh_0_low_: [%d]", hsv_thresh_0_low_);
    private_nh_.getParam("hsv_thresh_0_high", hsv_thresh_0_high_);
    ROS_INFO("hsv_thresh_0_high_: [%d]", hsv_thresh_0_high_);

    private_nh_.getParam("hsv_thresh_1_low", hsv_thresh_1_low_);
    ROS_INFO("hsv_thresh_1_low_: [%d]", hsv_thresh_1_low_);
    private_nh_.getParam("hsv_thresh_1_high", hsv_thresh_1_high_);
    ROS_INFO("hsv_thresh_1_high_: [%d]", hsv_thresh_1_high_);

    private_nh_.getParam("hsv_thresh_2_low", hsv_thresh_2_low_);
    ROS_INFO("hsv_thresh_2_low_: [%d]", hsv_thresh_2_low_);
    private_nh_.getParam("hsv_thresh_2_high", hsv_thresh_2_high_);
    ROS_INFO("hsv_thresh_2_high_: [%d]", hsv_thresh_2_high_);

    private_nh_.getParam("afa_thresh", afa_thresh_);
    ROS_INFO("afa_thresh_: [%lf]", afa_thresh_);
    private_nh_.getParam("area_thresh", area_thresh_);
    ROS_INFO("area_thresh_: [%d]", area_thresh_);

    if(is_rtsp_){
        gstreamer_ = std::make_shared<GStreamerWrapper>();
        detect_thread_ = std::thread(&BallDetector::DetectThread, this);
    }
    else{
        image_sub_ = nh_.subscribe<sensor_msgs::Image>(img_topic_, 10, &BallDetector::ImageCB, this);
    }
    ball_circle_pub_ = nh_.advertise<football::circle>(box_topic_, 10);
}

void BallDetector::ImageCB(const sensor_msgs::ImageConstPtr &msgRGB)
{
    cv_bridge::CvImageConstPtr cv_ptrRGB;
    try{
        cv_ptrRGB = cv_bridge::toCvCopy(msgRGB, "bgr8");
    }
    catch(cv_bridge::Exception &e){
        ROS_ERROR("cv_bridge exception: %s", e.what());
        return;
    }
    frame_width_ = msgRGB->width;
    frame_height_ = msgRGB->height;
    DetectBall(cv_ptrRGB->image);
}

void BallDetector::DetectThread(){
    std::tuple<int,int> frame_size = gstreamer_->GetFrameSize();
    frame_width_ = std::get<0>(frame_size);
    frame_height_ = std::get<1>(frame_size);
    cv::Mat frame(cv::Size(frame_width_, frame_height_), CV_8UC3);
    while(ros::ok()){
        bool ret = gstreamer_->GetFrame(frame);
        if(ret){
            DetectBall(frame);
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
}

void BallDetector::DetectBall(const cv::Mat &img){
    const cv::Mat &rgb_img = img;

    //hsv通道提取与阈值处理
    cv::Mat hsv_img;
    cvtColor(rgb_img, hsv_img, CV_BGR2HSV);
    std::vector<cv::Mat> hsvChannels;
    split(hsv_img, hsvChannels);
    cv::Mat bi = (hsvChannels[0] >= hsv_thresh_0_low_) & (hsvChannels[0] <= hsv_thresh_0_high_) 
                & (hsvChannels[1] >= hsv_thresh_1_low_) & (hsvChannels[1] <= hsv_thresh_1_high_) 
                & (hsvChannels[2] >= hsv_thresh_2_low_) & (hsvChannels[2] <= hsv_thresh_2_high_);
    if(is_debug_){
        imshow("bi", bi);
    }

    //高斯模糊
    cv::Mat gauss;
    cv::GaussianBlur(bi, gauss, cv::Size(5, 5), 2, 2);
    if(is_debug_){
        imshow("gauss", gauss);
    }

    cv::Mat element;
    element = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(5,5));

    //腐蚀
    cv::Mat eroded;
    cv::erode(gauss, eroded, element);
    if(is_debug_){    
        cv::imshow("eroded", eroded);
    }

    //膨胀
    cv::Mat dilated;
    cv::dilate(eroded, dilated, element);
    if(is_debug_){
        cv::imshow("dilated", dilated);
    }    

    //寻找最大轮廓
    std::vector<std::vector<cv::Point>> contours;
    std::vector<cv::Vec4i> hierarchy;
    std::vector<cv::Point> max_c;
    cv::findContours(dilated, contours, hierarchy, cv::RETR_LIST, cv::CHAIN_APPROX_SIMPLE, cv::Point());//寻找物体轮廓
    int maxarea = 0;
    for(int i=0; i<int(contours.size()); i++){
        int area = cv::contourArea(contours[i]);    //计算轮廓的面积
        if(area > maxarea){
            maxarea = area;
            max_c = contours[i];
        }
    }

    //对最大轮廓进行处理
    if(maxarea > area_thresh_){
        float s = cv::contourArea(max_c);
        float c = cv::arcLength(max_c, true);
        float afa = abs((4*M_PI*s/(c*c)) - 1);          //计算是否是圆形
        if(afa < afa_thresh_){
            cv::Point2f center;
            float radius;
            cv::minEnclosingCircle(max_c, center, radius);  //寻找包裹轮廓的最小圆
            football::circle ball_circle;
            ball_circle.center_x = center.x;
            ball_circle.center_y = center.y;
            ball_circle.radius = radius;
            ball_circle.frame_width = frame_width_;
            ball_circle.frame_height = frame_height_;
            ball_circle_last_ = ball_circle;
            ball_circle_pub_.publish(ball_circle);

            cv::Scalar color = cv::Scalar(255, 0, 0);
            circle(rgb_img, center, radius, color, 2);
            circle(rgb_img, center, 2, color, -1);
        }
        else{
            ROS_INFO("afa : %f", afa);
        }
    }
    else{
        // 发布非法值
        football::circle ball_circle;
        ball_circle.center_x = kNoBall;
        ball_circle.center_y = kNoBall;
        ball_circle.radius = kNoBall;
        ball_circle.frame_width = frame_width_;
        ball_circle.frame_height = frame_height_;    
        ball_circle_pub_.publish(ball_circle);
    }

    cv::imshow("Image window", rgb_img);
    cv::waitKey(1);
}
