#include <cmath>
#include <string>

#include <nav_msgs/Odometry.h>
#include <ros/ros.h>
#include <tf/transform_datatypes.h>

namespace
{
constexpr double kDegToRad = M_PI / 180.0;

class Lite3LidarPoseAdapter
{
public:
  Lite3LidarPoseAdapter()
      : nh_(),
        pnh_("~")
  {
    pnh_.param<std::string>("body_odom_topic", body_odom_topic_, "/leg_odom2");
    pnh_.param<std::string>("sensor_pose_topic", sensor_pose_topic_, "/scan_lite3/lidar_odom");
    pnh_.param<std::string>("frame_id", frame_id_, "odom");
    pnh_.param<std::string>("child_frame_id", child_frame_id_, "rslidar");

    pnh_.param("extrinsic_x", extrinsic_x_, 0.187);
    pnh_.param("extrinsic_y", extrinsic_y_, 0.0);
    pnh_.param("extrinsic_z", extrinsic_z_, 0.073);
    pnh_.param("extrinsic_roll_deg", extrinsic_roll_deg_, 0.0);
    pnh_.param("extrinsic_pitch_deg", extrinsic_pitch_deg_, 18.0);
    pnh_.param("extrinsic_yaw_deg", extrinsic_yaw_deg_, 0.0);

    body_odom_sub_ = nh_.subscribe(body_odom_topic_, 50, &Lite3LidarPoseAdapter::odomCallback, this,
                                   ros::TransportHints().tcpNoDelay());
    sensor_pose_pub_ = nh_.advertise<nav_msgs::Odometry>(sensor_pose_topic_, 10);

    ROS_WARN("[lite3_lidar_pose_adapter] %s -> %s, extrinsic xyz=(%.3f, %.3f, %.3f), rpy_deg=(%.1f, %.1f, %.1f)",
             body_odom_topic_.c_str(), sensor_pose_topic_.c_str(),
             extrinsic_x_, extrinsic_y_, extrinsic_z_,
             extrinsic_roll_deg_, extrinsic_pitch_deg_, extrinsic_yaw_deg_);
  }

private:
  void odomCallback(const nav_msgs::OdometryConstPtr &msg)
  {
    tf::Transform body_tf;
    tf::poseMsgToTF(msg->pose.pose, body_tf);

    tf::Quaternion q_ext;
    q_ext.setRPY(extrinsic_roll_deg_ * kDegToRad,
                 extrinsic_pitch_deg_ * kDegToRad,
                 extrinsic_yaw_deg_ * kDegToRad);
    q_ext.normalize();

    const tf::Transform lidar_ext(q_ext, tf::Vector3(extrinsic_x_, extrinsic_y_, extrinsic_z_));
    const tf::Transform lidar_tf = body_tf * lidar_ext;

    nav_msgs::Odometry out;
    out.header.stamp = msg->header.stamp.isZero() ? ros::Time::now() : msg->header.stamp;
    out.header.frame_id = frame_id_;
    out.child_frame_id = child_frame_id_;
    tf::poseTFToMsg(lidar_tf, out.pose.pose);
    out.twist = msg->twist;

    sensor_pose_pub_.publish(out);
  }

  ros::NodeHandle nh_;
  ros::NodeHandle pnh_;
  ros::Subscriber body_odom_sub_;
  ros::Publisher sensor_pose_pub_;

  std::string body_odom_topic_;
  std::string sensor_pose_topic_;
  std::string frame_id_;
  std::string child_frame_id_;
  double extrinsic_x_ = 0.187;
  double extrinsic_y_ = 0.0;
  double extrinsic_z_ = 0.073;
  double extrinsic_roll_deg_ = 0.0;
  double extrinsic_pitch_deg_ = 18.0;
  double extrinsic_yaw_deg_ = 0.0;
};
} // namespace

int main(int argc, char **argv)
{
  ros::init(argc, argv, "lite3_lidar_pose_adapter");
  Lite3LidarPoseAdapter node;
  ros::spin();
  return 0;
}
