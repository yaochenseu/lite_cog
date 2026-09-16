#include <ros/ros.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <global_planner/planner_core.h>
#include <scan_map_navigation/CheckPoses.h>
#include <nav_msgs/GetPlan.h>
#include <nav_msgs/Path.h>
#include <tf2_ros/transform_listener.h>
#include <tf/tf.h>
#include <cmath>
#include <algorithm>
#include <vector>

class MapPlanner {
  ros::NodeHandle nh_{"~"};
  tf2_ros::Buffer tf_;
  tf2_ros::TransformListener listener_{tf_};
  costmap_2d::Costmap2DROS costmap_{"global_costmap", tf_};
  global_planner::GlobalPlanner planner_;
  ros::ServiceServer plan_srv_, check_srv_;
  ros::Publisher path_pub_;
  double radius_, offset_;
public:
  MapPlanner() {
    nh_.param("body_radius", radius_, 0.35);
    nh_.param("body_offset", offset_, 0.18);
    planner_.initialize("GlobalPlanner", &costmap_);
    plan_srv_ = nh_.advertiseService("make_plan", &MapPlanner::plan, this);
    check_srv_ = nh_.advertiseService("check_poses", &MapPlanner::check, this);
    path_pub_ = nh_.advertise<nav_msgs::Path>("path", 1, true);
  }
  bool plan(nav_msgs::GetPlan::Request &req, nav_msgs::GetPlan::Response &res) {
    if (req.start.header.frame_id != costmap_.getGlobalFrameID() ||
        req.goal.header.frame_id != costmap_.getGlobalFrameID() || !costmap_.isCurrent())
      return false;
    auto *cm = costmap_.getCostmap();
    boost::unique_lock<costmap_2d::Costmap2D::mutex_t> lock(*cm->getMutex());
    res.plan.header.frame_id = costmap_.getGlobalFrameID();
    res.plan.header.stamp = ros::Time::now();
    // GlobalPlanner clears the start cell; do not permanently mutate the prior.
    const std::vector<unsigned char> saved(cm->getCharMap(),
        cm->getCharMap()+cm->getSizeInCellsX()*cm->getSizeInCellsY());
    const bool success=planner_.makePlan(req.start, req.goal, req.tolerance, res.plan.poses);
    std::copy(saved.begin(),saved.end(),cm->getCharMap());
    if (!success) return false;
    path_pub_.publish(res.plan);
    return true;
  }
  bool check(scan_map_navigation::CheckPoses::Request &req,
             scan_map_navigation::CheckPoses::Response &res) {
    res.safe = false;
    if (req.samples.header.frame_id != costmap_.getGlobalFrameID() ||
        req.samples.poses.empty() || !costmap_.isCurrent()) {
      res.message = "Static costmap unavailable or invalid frame/samples"; return true;
    }
    auto *cm = costmap_.getCostmap();
    boost::unique_lock<costmap_2d::Costmap2D::mutex_t> lock(*cm->getMutex());
    // Check the occupied area of BOTH SCAN cylinders, not merely polygon edges.
    // Reject unknown cells. Add half a cell diagonal for conservative rasterization.
    const double r = radius_ + cm->getResolution()*0.707107;
    for (const auto &pose : req.samples.poses) {
      double yaw = tf::getYaw(pose.orientation);
      if (!std::isfinite(pose.position.x) || !std::isfinite(pose.position.y) || !std::isfinite(yaw))
        return true;
      for (double sign : {-1.0, 1.0}) {
        const double x = pose.position.x + sign*offset_*std::cos(yaw);
        const double y = pose.position.y + sign*offset_*std::sin(yaw);
        unsigned int x0,y0,x1,y1;
        if (!cm->worldToMap(x-r,y-r,x0,y0) || !cm->worldToMap(x+r,y+r,x1,y1)) {
          res.message = "Footprint outside static map"; return true;
        }
        for (unsigned int i=x0;i<=x1;++i) for (unsigned int j=y0;j<=y1;++j) {
          double wx,wy; cm->mapToWorld(i,j,wx,wy);
          if (std::hypot(wx-x,wy-y)<=r && cm->getCost(i,j)>=costmap_2d::LETHAL_OBSTACLE) {
            res.message = "Footprint hits static obstacle/unknown"; return true;
          }
        }
      }
    }
    res.safe = true; return true;
  }
};
int main(int argc,char **argv) {
  ros::init(argc,argv,"scan_global");
  MapPlanner planner;
  ros::spin();
  return 0;
}
