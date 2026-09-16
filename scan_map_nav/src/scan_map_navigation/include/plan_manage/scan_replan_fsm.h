// Modified from local SCAN-Planner (2026-09-10): map navigation reset, checks and heartbeat.
#ifndef _SCAN_REPLAN_FSM_H_
#define _SCAN_REPLAN_FSM_H_

#include <Eigen/Eigen>
#include <algorithm>
#include <deque>
#include <geometry_msgs/PoseStamped.h>
#include <iostream>
#include <nav_msgs/Odometry.h>
#include <nav_msgs/Path.h>
#include <sensor_msgs/Imu.h>
#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Empty.h>
#include <std_srvs/Trigger.h>
#include <scan_map_navigation/CheckPoses.h>
#include <scan_map_navigation/LocalTarget.h>
#include <scan_map_navigation/LocalTrajectory.h>
#include <scan_map_navigation/NavigationControl.h>
#include <scan_map_navigation/PlannerState.h>
#include <std_srvs/SetBool.h>
#include <vector>
#include <visualization_msgs/Marker.h>

#include <bspline_opt/bspline_optimizer.h>
#include <plan_env/grid_map.h>
#include <scan_planner/Bspline.h>
#include <scan_planner/DataDisp.h>
#include <plan_manage/planner_manager.h>
#include <traj_utils/planning_visualization.h>

using std::vector;

namespace scan_planner
{

  class SCANReplanFSM
  {

  private:
    /* ---------- flag ---------- */
    enum FSM_EXEC_STATE
    {
      INIT,
      WAIT_TARGET,
      GEN_NEW_TRAJ,
      REPLAN_TRAJ,
      EXEC_TRAJ,
      EMERGENCY_STOP
    };
    enum NAVI_MODE
    {
      MANUAL_TARGET = 1,
      PRESET_TARGET = 2,
      REFERENCE_PATH = 3,
      ROLLING_TARGET = 4,
    };

    /* planning utils */
    SCANPlannerManager::Ptr planner_manager_;
    PlanningVisualization::Ptr visualization_;
    scan_planner::DataDisp data_disp_;

    /* parameters */
    int navi_mode_; // 1 manual select, 2 hard code
    double no_replan_thresh_, replan_thresh_;
    std::vector<Eigen::Vector3d> preset_waypoints_;
    int waypoint_num_;
    double planning_horizon_;
    double emergency_time_;
    double rviz_goal_height_;
    double self_inflation_z_up_, self_inflation_z_down_;
    double self_double_cylinder_radius_, self_double_cylinder_offset_;
    double body_height_;
    std::string self_inflation_frame_id_;
    bool recovery_enabled_;
    int recovery_trigger_fail_count_, recovery_max_attempts_;
    double recovery_distance_, recovery_waypoint_spacing_, recovery_goal_tolerance_;

    /* planning data */
    bool trigger_, have_target_, have_odom_, have_new_target_;
    bool rviz_height_ready_;
    bool go2_execution_frozen_;
    bool enable_fail_safe_, need_hover_stop_;
    FSM_EXEC_STATE exec_state_;
    int continuously_called_times_{0};
    int replan_fail_count_{0};
    int max_replan_fail_count_{1000};
    bool recovery_active_{false};
    int recovery_attempt_count_{0};
    Eigen::Vector3d recovery_saved_goal_;
    std::deque<Eigen::Vector3d> recovery_breadcrumb_;
    ros::Time last_freeze_update_time_;

    Eigen::Vector3d odom_pos_, odom_vel_, odom_acc_; // odometry state
    Eigen::Quaterniond odom_orient_;

    Eigen::Vector3d init_pt_, start_pt_, start_vel_, start_acc_, start_yaw_; // start state
    Eigen::Vector3d end_pt_, end_vel_;                                       // goal state
    Eigen::Vector3d local_target_pt_, local_target_vel_;                     // local target state
    std::vector<Eigen::Vector3d> active_waypoints_;
    int current_wp_;

    bool flag_escape_emergency_;

    /* ROS utils */
    ros::NodeHandle node_;
    ros::ServiceServer reset_srv_, check_srv_;
    ros::Publisher heartbeat_pub_;
    ros::Publisher tagged_traj_pub_;
    ros::Publisher planner_state_pub_;
    uint64_t execution_generation_{0};
    uint64_t recovery_target_id_{0};
    bool local_hold_{false}, local_blocked_{false}, checked_trajectory_{false};
    bool test_obstacle_{false};
    ros::ServiceServer test_obstacle_srv_;
    ros::WallTime local_recovery_started_, local_retry_at_;
    int local_attempts_{0}, local_max_attempts_{20};
    double local_recovery_timeout_{3.0}, local_retry_period_{0.1};
    std::string local_reason_;
    void beginLocalRecovery(const std::string &reason);
    void runLocalRecovery();
    void publishPlannerState();
    bool validateLocalTrajectory();
    ros::Subscriber rolling_target_sub_, control_sub_;
    scan_map_navigation::NavigationControl navigation_control_;
    uint64_t rolling_task_id_{0};
    uint32_t rolling_epoch_{0};
    ros::Time target_accept_after_, last_target_stamp_;
    bool rolling_final_{true};
    void rollingTargetCallback(const scan_map_navigation::LocalTarget::ConstPtr &);
    void publishTaggedTrajectory(const scan_planner::Bspline &);
    ros::Timer heartbeat_timer_;
    bool resetCallback(std_srvs::Trigger::Request &, std_srvs::Trigger::Response &);
    bool checkPosesCallback(scan_map_navigation::CheckPoses::Request &, scan_map_navigation::CheckPoses::Response &);
    ros::Timer exec_timer_, safety_timer_;
    ros::Subscriber goal_sub_, odom_sub_, path_sub_, go2_execution_frozen_sub_;
    ros::Publisher replan_pub_, new_pub_, bspline_pub_, data_disp_pub_, self_inflation_pub_, recovery_state_pub_;

    /* helper functions */
    bool callReboundReplan(bool flag_use_poly_init, bool flag_randomPolyTraj); // front-end and back-end method
    bool callEmergencyStop(Eigen::Vector3d stop_pos);                          // front-end and back-end method
    bool planFromCurrentTraj();
    void setStartStateFromOdomOrCurrentTraj();

    /* return value: std::pair< Times of the same state be continuously called, current continuously called state > */
    void changeFSMExecState(FSM_EXEC_STATE new_state, string pos_call);
    std::pair<int, SCANReplanFSM::FSM_EXEC_STATE> timesOfConsecutiveStateCalls();
    void printFSMExecState();

    void planGlobalTrajbyGivenWps();
    bool planGlobalTrajByWaypoints(const std::vector<Eigen::Vector3d> &waypoints,
                                   bool stop_at_start = false);
    bool planNextWaypoint();
    bool isWaypointSequenceMode() const;
    bool adjustGlobalTargetIfOccupied();
    void getLocalTarget();
    void finishProcess();
    void publishSelfInflationMarker();
    double getOdomYaw() const;
    double estimateYawFromSegment(const Eigen::Vector3d &from, const Eigen::Vector3d &to) const;
    void updateLocalTrajTimeFreeze();
    void resetRecoveryForNewGoal();
    void recordRecoveryBreadcrumb();
    void publishRecoveryState();
    bool startDeadEndRecovery();
    bool resumeGoalAfterRecovery();

    /* ROS functions */
    void execFSMCallback(const ros::TimerEvent &e);
    void checkCollisionCallback(const ros::TimerEvent &e);
    void rvizGoalCallback(const geometry_msgs::PoseStampedConstPtr &msg);
    void waypointCallback(const nav_msgs::PathConstPtr &msg);
    void pathCallback(const nav_msgs::PathConstPtr &msg);
    void odometryCallback(const nav_msgs::OdometryConstPtr &msg);
    void go2ExecutionFrozenCallback(const std_msgs::BoolConstPtr &msg);

    bool checkCollision();

  public:
    SCANReplanFSM(/* args */)
    {
    }
    ~SCANReplanFSM()
    {
    }

    void init(ros::NodeHandle &nh);

    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  };

} // namespace scan_planner

#endif
