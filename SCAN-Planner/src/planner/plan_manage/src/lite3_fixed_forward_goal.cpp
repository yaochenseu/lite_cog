#include <cmath>
#include <sstream>
#include <string>

#include <geometry_msgs/PoseStamped.h>
#include <nav_msgs/Odometry.h>
#include <ros/ros.h>
#include <std_srvs/Trigger.h>
#include <tf/tf.h>

#include "scan_planner/SetRelativeGoal.h"

namespace
{
class Lite3FixedForwardGoal
{
public:
  Lite3FixedForwardGoal()
      : nh_(),
        pnh_("~")
  {
    pnh_.param<std::string>("odom_topic", odom_topic_, "/leg_odom2");
    pnh_.param<std::string>("goal_topic", goal_topic_, "/move_base_simple/goal");
    pnh_.param<std::string>("goal_frame_id", goal_frame_id_, "odom");
    pnh_.param("distance", distance_, 1.0);
    pnh_.param("max_relative_distance", max_relative_distance_, 5.0);
    pnh_.param("auto_send", auto_send_, false);
    pnh_.param("auto_send_delay", auto_send_delay_, 1.0);

    odom_sub_ = nh_.subscribe(odom_topic_, 20, &Lite3FixedForwardGoal::odomCallback, this,
                              ros::TransportHints().tcpNoDelay());
    goal_pub_ = nh_.advertise<geometry_msgs::PoseStamped>(goal_topic_, 1, true);
    trigger_srv_ = pnh_.advertiseService("send_goal", &Lite3FixedForwardGoal::sendGoalService, this);
    relative_goal_srv_ = pnh_.advertiseService(
        "send_relative_goal", &Lite3FixedForwardGoal::sendRelativeGoalService, this);
    auto_timer_ = nh_.createTimer(ros::Duration(0.1), &Lite3FixedForwardGoal::autoSendTimer, this);
    start_time_ = ros::Time::now();

    ROS_WARN("[lite3_fixed_forward_goal] ready. Default: rosservice call %s/send_goal; "
             "relative: rosservice call %s/send_relative_goal '{forward: 1.0, left: 0.0}'",
             ros::this_node::getName().c_str(), ros::this_node::getName().c_str());
  }

private:
  void odomCallback(const nav_msgs::OdometryConstPtr &msg)
  {
    latest_odom_ = *msg;
    have_odom_ = true;
  }

  bool buildAndPublishGoal(double forward, double left,
                           geometry_msgs::PoseStamped &goal, std::string &message)
  {
    if (!have_odom_)
    {
      message = "no odom received yet from " + odom_topic_;
      return false;
    }

    if (!std::isfinite(forward) || !std::isfinite(left))
    {
      message = "relative goal contains a non-finite value";
      return false;
    }

    const double relative_distance = std::hypot(forward, left);
    if (relative_distance < 0.05)
    {
      message = "relative goal is too close; distance must be at least 0.05 m";
      return false;
    }
    if (max_relative_distance_ > 0.0 && relative_distance > max_relative_distance_)
    {
      std::ostringstream oss;
      oss << "relative goal distance " << relative_distance
          << " m exceeds limit " << max_relative_distance_ << " m";
      message = oss.str();
      return false;
    }

    const auto &pose = latest_odom_.pose.pose;
    const double yaw = tf::getYaw(pose.orientation);
    if (!std::isfinite(yaw))
    {
      message = "odom yaw is not finite";
      return false;
    }

    goal.header.stamp = ros::Time::now();
    goal.header.frame_id = goal_frame_id_;
    goal.pose.position.x = pose.position.x + forward * std::cos(yaw) - left * std::sin(yaw);
    goal.pose.position.y = pose.position.y + forward * std::sin(yaw) + left * std::cos(yaw);
    goal.pose.position.z = pose.position.z;
    const double travel_yaw = yaw + std::atan2(left, forward);
    goal.pose.orientation = tf::createQuaternionMsgFromYaw(travel_yaw);

    goal_pub_.publish(goal);
    sent_ = true;

    std::ostringstream oss;
    oss.setf(std::ios::fixed);
    oss.precision(3);
    oss << "sent relative goal: x=" << goal.pose.position.x
        << " y=" << goal.pose.position.y
        << " z=" << goal.pose.position.z
        << " travel_yaw=" << travel_yaw
        << " forward=" << forward
        << " left=" << left
        << " distance=" << relative_distance;
    message = oss.str();
    ROS_WARN_STREAM("[lite3_fixed_forward_goal] " << message);
    return true;
  }

  bool sendGoalService(std_srvs::Trigger::Request &, std_srvs::Trigger::Response &res)
  {
    geometry_msgs::PoseStamped goal;
    res.success = buildAndPublishGoal(distance_, 0.0, goal, res.message);
    return true;
  }

  bool sendRelativeGoalService(scan_planner::SetRelativeGoal::Request &req,
                               scan_planner::SetRelativeGoal::Response &res)
  {
    res.success = buildAndPublishGoal(req.forward, req.left, res.goal, res.message);
    return true;
  }

  void autoSendTimer(const ros::TimerEvent &)
  {
    if (!auto_send_ || sent_)
      return;
    if ((ros::Time::now() - start_time_).toSec() < auto_send_delay_)
      return;

    std::string message;
    geometry_msgs::PoseStamped goal;
    buildAndPublishGoal(distance_, 0.0, goal, message);
  }

  ros::NodeHandle nh_;
  ros::NodeHandle pnh_;
  ros::Subscriber odom_sub_;
  ros::Publisher goal_pub_;
  ros::ServiceServer trigger_srv_;
  ros::ServiceServer relative_goal_srv_;
  ros::Timer auto_timer_;

  std::string odom_topic_;
  std::string goal_topic_;
  std::string goal_frame_id_;
  double distance_ = 1.0;
  double max_relative_distance_ = 5.0;
  bool auto_send_ = false;
  double auto_send_delay_ = 1.0;
  ros::Time start_time_;

  nav_msgs::Odometry latest_odom_;
  bool have_odom_ = false;
  bool sent_ = false;
};
} // namespace

int main(int argc, char **argv)
{
  ros::init(argc, argv, "lite3_fixed_forward_goal");
  Lite3FixedForwardGoal node;
  ros::spin();
  return 0;
}
