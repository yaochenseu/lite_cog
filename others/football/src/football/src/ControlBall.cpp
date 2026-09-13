
#include <ros/ros.h>
#include <football/circle.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Int32.h>

#include "BallState.h"

using namespace std;

ros::Subscriber Control_sub;
ros::Publisher Control_pub;
ros::Publisher Kick_pub;

#define MAXR 1.0
#define MAXV 1.0

int close_enough_count = 0;
bool hasKicked = false;
int rotate_count = 0;
int close_count = 0;
int find_count = 0;

#define LEFT_FOOT 0
#define RIGHT_FOOT 2

bool kick_toggle = 1;
int r_times = 0;
int v_times = 0;

void kickBall(int foot)
{
    std_msgs::Int32 kickMsg;
    kick_toggle = !kick_toggle;
    kickMsg.data = foot + kick_toggle;
    ROS_INFO("kickBall kickMsg.data: [%d]", kickMsg.data);
    Kick_pub.publish(kickMsg);
}

int detected_count = 0;
bool steady_detected = 0;

//读取球的位置和半径，发送速度
void controlCb(const football::circle msg)
{
    float delta_x;
    float vel_v, vel_r;
    if(msg.center_x != kNoBall)    //Ball is in the image
    {
        if(detected_count++ == 10){
            close_enough_count = 0;
            steady_detected = true;
        }
        
        if(steady_detected == true){
            hasKicked = false;
            delta_x = -(msg.center_x-msg.frame_width/2)/(msg.frame_width/2);
            if(msg.center_y < 0.49 * msg.frame_height)  //Too Far
            {
                vel_v = MAXV;
                vel_r = delta_x * MAXR;
            }
            else if(msg.center_y < 0.9 * msg.frame_height)   //Far
            {
                vel_v = 0.12*MAXV+(1-(msg.center_y-0.49*msg.frame_height)/(0.51*msg.frame_height))*0.88*MAXV;
                vel_r = delta_x * MAXR;
            }
            else    //Close
            {
                vel_v = 0.12 * MAXV;
                vel_r = delta_x * MAXR;
            }
        }
    }
    else  //No ball in the image
    {
        steady_detected = false;

        detected_count = 0;
        ROS_INFO("Lost because close enough");
        close_enough_count++;
        if(close_enough_count > 10000){
            close_enough_count = 1000;
        }

        if(!hasKicked){
            if(close_enough_count < close_count)
            {
                ROS_INFO("get close to ball");
                vel_v = 0.01 * v_times;
                vel_r = -3.14 / 180 * r_times;
            }
            else
            {
                ROS_INFO("Kick on left foot");
                kickBall(LEFT_FOOT);
                close_enough_count = 0;
                hasKicked = true;
                find_count = 0;
                vel_v = 0.0;
                vel_r = 0.0;
            }
        }
        else
        {
            find_count++;
            if(find_count < 60){
                vel_v = 0;
                vel_r = 0;
            }
            else{
                vel_v = -0.5;
                vel_r = 0;
            }
        }
    }

    geometry_msgs::Twist vel_msg;
    vel_msg.linear.x = vel_v;
    vel_msg.angular.z = vel_r;
    Control_pub.publish(vel_msg);

    ROS_INFO("close_enough_count: [%d], vel_v [%f], vel_r: [%f]", close_enough_count, vel_v, vel_r);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "control_ball");
    ros::NodeHandle nh;
    ros::NodeHandle private_nh("~");
    private_nh.getParam("rotate_count", rotate_count);
    ROS_INFO("rotate_count: [%d]", rotate_count);
    private_nh.getParam("close_count", close_count);
    ROS_INFO("close_count: [%d]", close_count);
    private_nh.getParam("v_times", v_times);
    ROS_INFO("v_times: [%d]", v_times);
    private_nh.getParam("r_times", r_times);
    ROS_INFO("r_times: [%d]", r_times);    
    Control_sub = nh.subscribe<football::circle>("/ball_track_box_realsense", 1, controlCb);
	Control_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
    Kick_pub = nh.advertise<std_msgs::Int32>("/kick_ball", 1);
    ros::spin();
    return 0;
}


