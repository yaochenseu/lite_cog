// Modified from local SCAN-Planner (2026-09-10): persistent map-derived reference
// path, body velocity conversion, reset/footprint services and planner heartbeat.
#include <plan_manage/scan_replan_fsm.h>
#include <cmath>
#include <cstdlib>

namespace
{
  std::string shellQuote(const std::string &value)
  {
    std::string quoted = "'";
    for (const char c : value)
    {
      if (c == '\'')
        quoted += "'\\''";
      else
        quoted += c;
    }
    quoted += "'";
    return quoted;
  }
} // namespace

namespace scan_planner
{

  void SCANReplanFSM::init(ros::NodeHandle &nh)
  {
    current_wp_ = 0;
    exec_state_ = FSM_EXEC_STATE::INIT;
    trigger_ = false;
    have_target_ = false;
    have_odom_ = false;
    have_new_target_ = false;
    rviz_height_ready_ = false;
    go2_execution_frozen_ = false;
    flag_escape_emergency_ = true;
    need_hover_stop_ = false;
    replan_fail_count_ = 0;
    recovery_active_ = false;
    recovery_attempt_count_ = 0;
    last_freeze_update_time_ = ros::Time::now();

    /*  fsm param  */
    nh.param("fsm/navi_mode", navi_mode_, -1);
    nh.param("fsm/thresh_replan", replan_thresh_, -1.0);
    nh.param("fsm/thresh_no_replan", no_replan_thresh_, -1.0);
    nh.param("fsm/planning_horizon", planning_horizon_, -1.0);
    nh.param("fsm/emergency_time_", emergency_time_, 1.0);
    nh.param("fsm/fail_safe", enable_fail_safe_, true);
    nh.param("fsm/max_replan_fail_count", max_replan_fail_count_, 1000);
    nh.param("fsm/local_recovery_timeout", local_recovery_timeout_, 3.0);
    nh.param("fsm/local_retry_period", local_retry_period_, 0.1);
    nh.param("fsm/local_recovery_attempts", local_max_attempts_, 20);
    local_recovery_timeout_ = std::max(0.1, local_recovery_timeout_);
    local_retry_period_ = std::max(0.02, local_retry_period_);
    local_max_attempts_ = std::max(1, local_max_attempts_);
    nh.param("fsm/recovery_enabled", recovery_enabled_, true);
    nh.param("fsm/recovery_trigger_fail_count", recovery_trigger_fail_count_, 8);
    nh.param("fsm/recovery_max_attempts", recovery_max_attempts_, 2);
    nh.param("fsm/recovery_distance", recovery_distance_, 0.8);
    nh.param("fsm/recovery_waypoint_spacing", recovery_waypoint_spacing_, 0.25);
    nh.param("fsm/recovery_goal_tolerance", recovery_goal_tolerance_, 0.18);
    recovery_trigger_fail_count_ = std::max(1, recovery_trigger_fail_count_);
    recovery_max_attempts_ = std::max(1, recovery_max_attempts_);
    recovery_distance_ = std::max(0.3, recovery_distance_);
    recovery_waypoint_spacing_ = std::max(0.1, recovery_waypoint_spacing_);
    recovery_goal_tolerance_ = std::max(0.1, recovery_goal_tolerance_);
    nh.param("grid_map/obstacles_inflation_z_up", self_inflation_z_up_, 0.0);
    nh.param("grid_map/obstacles_inflation_z_down", self_inflation_z_down_, 0.0);
    nh.param("grid_map/double_cylinder_radius", self_double_cylinder_radius_, 0.0);
    nh.param("grid_map/double_cylinder_offset", self_double_cylinder_offset_, 0.0);
    nh.param("grid_map/double_cylinder_offset", body_height_, 0.4);
    nh.param("grid_map/frame_id", self_inflation_frame_id_, std::string("world"));

    if (navi_mode_ == NAVI_MODE::PRESET_TARGET)
    {
      const std::string keypoints_yaml = "\"$(rospack find scan_planner)/../../../tools/keypoint.yaml\"";
      const std::string load_keypoints_cmd =
          "rosparam load " + keypoints_yaml + " " + shellQuote(nh.getNamespace());
      if (std::system(load_keypoints_cmd.c_str()) != 0)
      {
        ROS_ERROR("[SCANReplanFSM] Failed to load keypoints_yaml: tools/keypoint.yaml");
        ros::shutdown();
        return;
      }

      nh.param("fsm/waypoint_num", waypoint_num_, -1);

      if (waypoint_num_ <= 0)
      {
        ROS_ERROR("[SCANReplanFSM] navi_mode=2 requires keypoints_yaml with fsm/waypoint_num and fsm/waypoint{i}_{x,y,z}.");
        ros::shutdown();
        return;
      }
      preset_waypoints_.resize(waypoint_num_);
      for (int i = 0; i < waypoint_num_; i++)
      {
        nh.param("fsm/waypoint" + to_string(i) + "_x", preset_waypoints_[i](0), -1.0);
        nh.param("fsm/waypoint" + to_string(i) + "_y", preset_waypoints_[i](1), -1.0);
        nh.param("fsm/waypoint" + to_string(i) + "_z", preset_waypoints_[i](2), -1.0);
      }
    }

    /* initialize main modules */
    visualization_.reset(new PlanningVisualization(nh));
    planner_manager_.reset(new SCANPlannerManager);
    planner_manager_->initPlanModules(nh, visualization_);

    /* callback */
    exec_timer_ = nh.createTimer(ros::Duration(0.01), &SCANReplanFSM::execFSMCallback, this);
    safety_timer_ = nh.createTimer(ros::Duration(0.05), &SCANReplanFSM::checkCollisionCallback, this);

    std::string body_pose_topic;
    ros::param::param<std::string>("/body_pose_topic", body_pose_topic, std::string("/quad_0/body_pose"));
    odom_sub_ = nh.subscribe(body_pose_topic, 1, &SCANReplanFSM::odometryCallback, this);
    go2_execution_frozen_sub_ = nh.subscribe("/planning/go2_execution_frozen", 10, &SCANReplanFSM::go2ExecutionFrozenCallback, this);

    bspline_pub_ = nh.advertise<scan_planner::Bspline>("/planning/bspline", 10);
    tagged_traj_pub_ = nh.advertise<scan_map_navigation::LocalTrajectory>("/scan_map_nav/local_trajectory", 1);
    planner_state_pub_ = nh.advertise<scan_map_navigation::PlannerState>("/scan_map_nav/planner_state", 1, true);
    control_sub_ = nh.subscribe<scan_map_navigation::NavigationControl>("/scan_map_nav/control", 1,
        [this](const scan_map_navigation::NavigationControl::ConstPtr &msg) {
          if (msg->task_id >= navigation_control_.task_id && msg->header.frame_id == "odom" && std::isfinite(msg->yaw))
          {
            navigation_control_ = *msg;
            publishPlannerState();
          }
        });
    data_disp_pub_ = nh.advertise<scan_planner::DataDisp>("/planning/data_display", 100);
    self_inflation_pub_ = nh.advertise<visualization_msgs::Marker>("self_inflation", 10, true);
    recovery_state_pub_ = nh.advertise<std_msgs::Bool>("/planning/recovery_active", 10, true);
    publishRecoveryState();

    reset_srv_ = nh.advertiseService("reset", &SCANReplanFSM::resetCallback, this);
    check_srv_ = nh.advertiseService("check_poses", &SCANReplanFSM::checkPosesCallback, this);
    heartbeat_pub_ = nh.advertise<std_msgs::Bool>("heartbeat", 1);
    // Same callback queue as planning: a blocked/crashed planner loses heartbeat.
    heartbeat_timer_ = nh.createTimer(ros::Duration(0.05), [this](const ros::TimerEvent &) {
      std_msgs::Bool m;
      // A live planner in local recovery is NOT a failed input.
      m.data = have_odom_;
      heartbeat_pub_.publish(m);
      publishPlannerState();
    });
    // Deterministic fault injection is available only on the isolated test
    // launch. It is not registered in normal navigation.
    bool test_hooks = false;
    nh.param("enable_test_hooks", test_hooks, false);
    std::string output_topic;
    nh.getParam("/scan_velocity_gate/output_topic", output_topic);
    if (test_hooks && output_topic == "/test/cmd_vel")
      test_obstacle_srv_ = nh.advertiseService<std_srvs::SetBool::Request, std_srvs::SetBool::Response>(
          "test_obstacle", [this](std_srvs::SetBool::Request &req, std_srvs::SetBool::Response &res) {
            test_obstacle_ = req.data;
            if (req.data && have_target_)
              beginLocalRecovery("TEST: obstacle invalidates candidate");
            res.success = true;
            return true;
          });

    if (navi_mode_ == NAVI_MODE::MANUAL_TARGET)
      goal_sub_ = nh.subscribe("/move_base_simple/goal", 1, &SCANReplanFSM::rvizGoalCallback, this);
    else if (navi_mode_ == NAVI_MODE::PRESET_TARGET)
    {
      ros::Duration(1.0).sleep();
      while (ros::ok() && !have_odom_)
        ros::spinOnce();
      planGlobalTrajbyGivenWps();
    }
    else if (navi_mode_ == NAVI_MODE::REFERENCE_PATH)
      path_sub_ = nh.subscribe("/initial_path", 1, &SCANReplanFSM::pathCallback, this);
    else if (navi_mode_ == NAVI_MODE::ROLLING_TARGET)
      rolling_target_sub_ = nh.subscribe("/scan_map_nav/local_target", 1, &SCANReplanFSM::rollingTargetCallback, this);
    else
      cout << "Wrong navi_mode_ value! navi_mode_=" << navi_mode_ << endl;
  }

  void SCANReplanFSM::publishPlannerState()
  {
    using State = scan_map_navigation::PlannerState;
    State msg;
    msg.header.stamp = ros::Time::now();
    msg.header.frame_id = self_inflation_frame_id_;
    msg.task_id = navigation_control_.task_id;
    msg.epoch = navigation_control_.epoch;
    msg.generation = execution_generation_;
    msg.target_revision = recovery_target_id_;
    msg.recovery_attempts = local_attempts_;
    msg.state = State::IDLE;
    if (have_odom_ && navigation_control_.mode == scan_map_navigation::NavigationControl::ALIGN)
    {
      bool safe = true;
      const double yaw = getOdomYaw();
      const double delta = std::atan2(std::sin(navigation_control_.yaw-yaw), std::cos(navigation_control_.yaw-yaw));
      const int steps = std::max(1,static_cast<int>(std::ceil(std::abs(delta)/0.05)));
      for (int i=0;i<=steps && safe;++i)
        safe = planner_manager_->grid_map_->getInflateOccupancy(odom_pos_,yaw+delta*i/steps) == 0;
      msg.state = safe ? State::ALIGNING : State::BLOCKED;
      msg.reason = safe ? "Final yaw checked" : "Final rotation footprint blocked";
    }
    else if (have_odom_ && navigation_control_.mode == scan_map_navigation::NavigationControl::TRACK &&
             rolling_task_id_ == msg.task_id && rolling_epoch_ == msg.epoch)
    {
      if (local_blocked_)
        msg.state = State::BLOCKED;
      else if (local_hold_)
        msg.state = State::RECOVERING;
      else
        msg.state = checked_trajectory_ ? State::TRACKING : State::PLANNING;
      msg.reason = local_reason_;
    }
    planner_state_pub_.publish(msg);
  }

  void SCANReplanFSM::beginLocalRecovery(const std::string &reason)
  {
    if (local_hold_ || local_blocked_)
      return;
    ++execution_generation_; // old splines AND queued velocities are revoked
    checked_trajectory_ = false;
    local_hold_ = true;
    local_blocked_ = false;
    local_attempts_ = 0;
    local_recovery_started_ = ros::WallTime::now();
    local_retry_at_ = ros::WallTime(0);
    local_reason_ = reason;
    publishPlannerState(); // send hold before starting any expensive planning
    ROS_WARN("Local recovery generation %lu: %s; replanning immediately from measured motion",
             static_cast<unsigned long>(execution_generation_),reason.c_str());
  }

  void SCANReplanFSM::runLocalRecovery()
  {
    if (local_blocked_ || navigation_control_.mode != scan_map_navigation::NavigationControl::TRACK ||
        navigation_control_.task_id != rolling_task_id_ || navigation_control_.epoch != rolling_epoch_)
      return;
    const auto now = ros::WallTime::now();
    if ((now-local_recovery_started_).toSec() >= local_recovery_timeout_ || local_attempts_ >= local_max_attempts_)
    {
      local_blocked_ = true;
      local_reason_ = "Local recovery budget exhausted: " + local_reason_;
      publishPlannerState();
      ROS_WARN("%s",local_reason_.c_str());
      return;
    }
    if (now < local_retry_at_)
      return;
    local_retry_at_ = now+ros::WallDuration(local_retry_period_);
    ++local_attempts_;
    // No standstill/quality confirmation stage. Start NOW with measured
    // velocity, not the velocity of the invalidated spline or an assumed zero.
    start_pt_ = odom_pos_;
    start_vel_ = odom_vel_;
    start_acc_.setZero();
    bool success = planner_manager_->planGlobalTraj(start_pt_,start_vel_,start_acc_,end_pt_,
                                                   Eigen::Vector3d::Zero(),Eigen::Vector3d::Zero());
    if (success)
      success = callReboundReplan(true,local_attempts_ > 1);
    if (success)
    {
      need_hover_stop_ = false;
      replan_fail_count_ = 0;
      flag_escape_emergency_ = true;
      changeFSMExecState(EXEC_TRAJ,"LOCAL_RECOVERED");
      ROS_INFO("Local recovery accepted a checked new trajectory after %d attempts",local_attempts_);
    }
  }

  bool SCANReplanFSM::validateLocalTrajectory()
  {
    if (test_obstacle_)
      return false;
    auto info = &planner_manager_->local_data_;
    auto map = planner_manager_->grid_map_;
    if (!std::isfinite(info->duration_) || info->duration_ <= 0)
      return false;
    // Check the complete candidate, including its endpoint and initial turn.
    const double yaw = getOdomYaw();
    Eigen::Vector3d p0 = info->position_traj_.evaluateDeBoorT(0);
    Eigen::Vector3d p1 = info->position_traj_.evaluateDeBoorT(std::min(0.05,info->duration_));
    const double heading = estimateYawFromSegment(p0,p1);
    const double delta = std::atan2(std::sin(heading-yaw),std::cos(heading-yaw));
    const int turns = std::max(1,static_cast<int>(std::ceil(std::abs(delta)/0.05)));
    for (int i=0;i<=turns;++i)
      if (map->getInflateOccupancy(odom_pos_,yaw+delta*i/turns) != 0)
      {
        ROS_WARN_THROTTLE(1.0,"Candidate rejected: initial turn at xyz=(%.3f,%.3f,%.3f), yaw=%.3f",
                          odom_pos_.x(),odom_pos_.y(),odom_pos_.z(),yaw+delta*i/turns);
        return false;
      }
    const int steps = std::max(1,static_cast<int>(std::ceil(info->duration_/0.02)));
    for (int i=0;i<=steps;++i)
    {
      const double t = info->duration_*i/steps;
      Eigen::Vector3d p = info->position_traj_.evaluateDeBoorT(t);
      Eigen::Vector3d next = info->position_traj_.evaluateDeBoorT(std::min(t+0.02,info->duration_));
      const double h = i == steps ? estimateYawFromSegment(p1,p) : estimateYawFromSegment(p,next);
      if (!p.allFinite() || map->getInflateOccupancy(p,h) != 0)
      {
        ROS_WARN_THROTTLE(1.0,"Candidate rejected: trajectory t=%.3f/%.3f, xyz=(%.3f,%.3f,%.3f), yaw=%.3f",
                          t,info->duration_,p.x(),p.y(),p.z(),h);
        return false;
      }
      p1 = p;
    }
    return true;
  }

  void SCANReplanFSM::rollingTargetCallback(const scan_map_navigation::LocalTarget::ConstPtr &msg)
  {
    const double age = (ros::Time::now()-msg->header.stamp).toSec();
    if (!have_odom_ || msg->header.frame_id != self_inflation_frame_id_ ||
        !msg->task_id || msg->task_id < rolling_task_id_ || msg->header.stamp <= target_accept_after_ ||
        msg->header.stamp <= last_target_stamp_ || age < -0.2 || age > 0.7)
      return;
    Eigen::Vector3d target(msg->position.x,msg->position.y,odom_pos_(2));
    if (!target.allFinite())
      return;
    last_target_stamp_ = msg->header.stamp;
    const bool same_task = msg->task_id == rolling_task_id_ && msg->epoch == rolling_epoch_;
    const bool held = same_task && (local_hold_ || local_blocked_);
    const bool replacement = same_task && msg->recovery_id > recovery_target_id_ &&
        msg->expected_generation == execution_generation_ &&
        navigation_control_.task_id == msg->task_id && navigation_control_.epoch == msg->epoch &&
        navigation_control_.mode == scan_map_navigation::NavigationControl::TRACK;
    if (held && !replacement)
      return; // ordinary/old/unauthorized targets cannot thaw a recovery
    if (msg->recovery_id && !replacement)
      return;
    if (!replacement && same_task && rolling_final_ == msg->final_goal && (target-end_pt_).norm() < 0.03 &&
        (have_target_ || (target-odom_pos_).head<2>().norm() < 0.12))
      return; // repeated delivery is not a new planning request
    if (!same_task) {
      resetRecoveryForNewGoal();
      recovery_target_id_=0;
    }
    rolling_task_id_ = msg->task_id;
    rolling_epoch_ = msg->epoch;
    rolling_final_ = msg->final_goal;
    // Same-task updates preserve the executing spline and recovery bookkeeping.
    // No reset, no controller stop; the next spline replaces the old one.
    if (held) {
      end_pt_=target;
      recovery_target_id_=msg->recovery_id;
      // Revoke even queued commands from the previous recovery before planning.
      ++execution_generation_;
      checked_trajectory_=false;
      local_hold_=true; local_blocked_=false;
      local_attempts_=0; local_retry_at_=ros::WallTime(0);
      local_recovery_started_=ros::WallTime::now();
      local_reason_="Adaptive target accepted; checking new trajectory";
      trigger_=have_target_=have_new_target_=true;
      publishPlannerState();
      return; // runLocalRecovery uses current MEASURED pose/velocity, no standstill wait
    }
    if (!planner_manager_->planGlobalTraj(odom_pos_,odom_vel_,Eigen::Vector3d::Zero(),
                                        target,Eigen::Vector3d::Zero(),Eigen::Vector3d::Zero()))
    {
      ROS_WARN("Rolling target reference generation failed");
      return;
    }
    end_pt_=target;
    if (replacement) recovery_target_id_=msg->recovery_id;
    trigger_ = have_target_ = have_new_target_ = true;
    visualization_->displayGoalPoint(end_pt_,Eigen::Vector4d(0,0.5,0.5,1),0.3,0);
    if (exec_state_ == WAIT_TARGET)
      changeFSMExecState(GEN_NEW_TRAJ,"ROLLING_TARGET");
    else if (exec_state_ == EXEC_TRAJ)
      changeFSMExecState(REPLAN_TRAJ,"ROLLING_TARGET");
  }

  void SCANReplanFSM::publishTaggedTrajectory(const scan_planner::Bspline &spline)
  {
    scan_map_navigation::LocalTrajectory tagged;
    tagged.task_id = rolling_task_id_;
    tagged.epoch = rolling_epoch_;
    tagged.generation = execution_generation_;
    tagged.order = spline.order;
    tagged.traj_id = spline.traj_id;
    tagged.start_time = spline.start_time;
    tagged.knots = spline.knots;
    tagged.pos_pts = spline.pos_pts;
    tagged_traj_pub_.publish(tagged);
  }

  void SCANReplanFSM::planGlobalTrajbyGivenWps()
  {
    std::vector<Eigen::Vector3d> wps = preset_waypoints_;

    for (size_t i = 0; i < wps.size(); i++)
    {
      visualization_->displayGoalPoint(wps[i], Eigen::Vector4d(0, 0.5, 0.5, 1), 0.3, i);
      ros::Duration(0.001).sleep();
    }

    active_waypoints_ = wps;
    current_wp_ = 0;
    trigger_ = true;
    init_pt_ = odom_pos_;

    if (planNextWaypoint())
    {
      changeFSMExecState(GEN_NEW_TRAJ, "TRIG");
    }
    else
    {
      ROS_ERROR("Unable to generate global trajectory to first preset waypoint!");
    }
  }

  void SCANReplanFSM::rvizGoalCallback(const geometry_msgs::PoseStampedConstPtr &msg)
  {
    if (!msg)
      return;

    if (!rviz_height_ready_)
    {
      ROS_WARN("[SCANReplanFSM] Ignore RViz goal before receiving initial body pose.");
      return;
    }

    nav_msgs::PathPtr path(new nav_msgs::Path);
    path->header = msg->header;
    path->poses.push_back(*msg);
    waypointCallback(path);
  }

  void SCANReplanFSM::waypointCallback(const nav_msgs::PathConstPtr &msg)
  {
    if (!msg || msg->poses.empty())
    {
      ROS_WARN_THROTTLE(1.0, "[waypointCallback] Empty waypoint message, ignore.");
      return;
    }

    if (msg->poses[0].pose.position.z < -0.1)
      return;

    cout << "Triggered!" << endl;
    resetRecoveryForNewGoal();
    trigger_ = true;
    init_pt_ = odom_pos_;

    bool success = false;
    end_pt_ << msg->poses[0].pose.position.x, msg->poses[0].pose.position.y, rviz_goal_height_;
    success = planner_manager_->planGlobalTraj(odom_pos_, odom_vel_, Eigen::Vector3d::Zero(), end_pt_, Eigen::Vector3d::Zero(), Eigen::Vector3d::Zero());

    if (success)
      success = adjustGlobalTargetIfOccupied();

    visualization_->displayGoalPoint(end_pt_, Eigen::Vector4d(0, 0.5, 0.5, 1), 0.3, 0);

    if (success)
    {

      /*** display ***/
      constexpr double step_size_t = 0.1;
      int i_end = floor(planner_manager_->global_data_.global_duration_ / step_size_t);
      vector<Eigen::Vector3d> gloabl_traj(i_end);
      for (int i = 0; i < i_end; i++)
      {
        gloabl_traj[i] = planner_manager_->global_data_.global_traj_.evaluate(i * step_size_t);
      }

      end_vel_.setZero();
      have_target_ = true;
      have_new_target_ = true;

      /*** FSM ***/
      if (exec_state_ == WAIT_TARGET)
        changeFSMExecState(GEN_NEW_TRAJ, "TRIG");
      else if (exec_state_ == EXEC_TRAJ)
        changeFSMExecState(REPLAN_TRAJ, "TRIG");

      // visualization_->displayGoalPoint(end_pt_, Eigen::Vector4d(1, 0, 0, 1), 0.3, 0);
      visualization_->displayGlobalPathList(gloabl_traj, 0.1, 0);
    }
    else
    {
      ROS_ERROR("Unable to generate global trajectory!");
    }
  }

  bool SCANReplanFSM::planGlobalTrajByWaypoints(const std::vector<Eigen::Vector3d> &waypoints,
                                                bool stop_at_start)
  {
    if (waypoints.empty())
    {
      ROS_WARN("[planGlobalTrajByWaypoints] No waypoint to plan.");
      return false;
    }

    end_pt_ = waypoints.back();

    for (size_t i = 0; i < waypoints.size(); i++)
    {
      visualization_->displayGoalPoint(waypoints[i], Eigen::Vector4d(0, 0.5, 0.5, 1), 0.3, i);
      ros::Duration(0.001).sleep();
    }

    bool success = planner_manager_->planGlobalTrajWaypoints(
        odom_pos_,
        stop_at_start ? Eigen::Vector3d::Zero() : odom_vel_,
        Eigen::Vector3d::Zero(),
        waypoints,
        Eigen::Vector3d::Zero(),
        Eigen::Vector3d::Zero());

    if (!success)
    {
      ROS_ERROR("Unable to generate global trajectory from waypoints!");
      return false;
    }

    if (navi_mode_ != NAVI_MODE::REFERENCE_PATH && !adjustGlobalTargetIfOccupied())
      return false;

    constexpr double step_size_t = 0.1;
    int i_end = floor(planner_manager_->global_data_.global_duration_ / step_size_t);
    std::vector<Eigen::Vector3d> gloabl_traj(i_end);
    for (int i = 0; i < i_end; i++)
    {
      gloabl_traj[i] = planner_manager_->global_data_.global_traj_.evaluate(i * step_size_t);
    }

    end_vel_.setZero();
    have_target_ = true;
    have_new_target_ = true;
    visualization_->displayGlobalPathList(gloabl_traj, 0.1, 0);
    visualization_->displayGoalPoint(end_pt_, Eigen::Vector4d(0, 0.5, 0.5, 1), 0.3, static_cast<int>(waypoints.size()) - 1);

    return true;
  }

  bool SCANReplanFSM::planNextWaypoint()
  {
    if (current_wp_ < 0 || current_wp_ >= (int)active_waypoints_.size())
    {
      ROS_WARN("[navi_mode=%d] No active waypoint to plan.", navi_mode_);
      return false;
    }

    end_pt_ = active_waypoints_[current_wp_];
    setStartStateFromOdomOrCurrentTraj();

    bool success = planner_manager_->planGlobalTraj(
        start_pt_,
        start_vel_,
        start_acc_,
        end_pt_,
        Eigen::Vector3d::Zero(),
        Eigen::Vector3d::Zero());

    if (!success)
    {
      ROS_ERROR("[navi_mode=%d] Unable to generate trajectory to waypoint %d.", navi_mode_, current_wp_ + 1);
      return false;
    }

    if (!adjustGlobalTargetIfOccupied())
      return false;

    constexpr double step_size_t = 0.1;
    int i_end = floor(planner_manager_->global_data_.global_duration_ / step_size_t);
    std::vector<Eigen::Vector3d> gloabl_traj(i_end);
    for (int i = 0; i < i_end; i++)
    {
      gloabl_traj[i] = planner_manager_->global_data_.global_traj_.evaluate(i * step_size_t);
    }

    end_vel_.setZero();
    have_target_ = true;
    have_new_target_ = true;
    visualization_->displayGlobalPathList(gloabl_traj, 0.1, 0);
    visualization_->displayGoalPoint(end_pt_, Eigen::Vector4d(0, 0.5, 0.5, 1), 0.3, current_wp_);
    ROS_INFO("[navi_mode=%d] Planning to waypoint %d/%zu: [%.2f, %.2f, %.2f].",
             navi_mode_, current_wp_ + 1, active_waypoints_.size(), end_pt_(0), end_pt_(1), end_pt_(2));

    return true;
  }

  bool SCANReplanFSM::isWaypointSequenceMode() const
  {
    return navi_mode_ == NAVI_MODE::PRESET_TARGET;
  }

  bool SCANReplanFSM::adjustGlobalTargetIfOccupied()
  {
    auto map = planner_manager_->grid_map_;
    auto &global_data = planner_manager_->global_data_;
    const double duration = global_data.global_duration_;
    if (!map || duration < 1e-3)
      return true;

    constexpr double sample_dt = 0.05;
    const int sample_num = std::max(1, static_cast<int>(std::ceil(duration / sample_dt)));
    const Eigen::Vector3d final_pt = global_data.global_traj_.evaluate(duration);
    const Eigen::Vector3d final_prev = global_data.global_traj_.evaluate(duration * (sample_num - 1) / sample_num);
    const int final_occ = map->getInflateOccupancy(final_pt, estimateYawFromSegment(final_prev, final_pt));
    if (final_occ <= 0)
      return true;

    for (int i = sample_num; i >= 0; --i)
    {
      const double t = duration * i / sample_num;
      const double prev_t = duration * std::max(0, i - 1) / sample_num;
      const Eigen::Vector3d pt = global_data.global_traj_.evaluate(t);
      const Eigen::Vector3d prev_pt = global_data.global_traj_.evaluate(prev_t);

      if (map->getInflateOccupancy(pt, estimateYawFromSegment(prev_pt, pt)) == 0)
      {
        const Eigen::Vector3d raw_end = end_pt_;
        end_pt_ = pt;
        global_data.global_duration_ = t;
        global_data.last_progress_time_ = std::min(global_data.last_progress_time_, t);
        ROS_WARN("[global target] Target [%.2f, %.2f, %.2f] is occupied; use backward collision-free point [%.2f, %.2f, %.2f].",
                 raw_end(0), raw_end(1), raw_end(2), end_pt_(0), end_pt_(1), end_pt_(2));
        return true;
      }
    }

    ROS_ERROR("[global target] Target is occupied, and no collision-free point was found along the global trajectory.");
    return false;
  }

  void SCANReplanFSM::pathCallback(const nav_msgs::PathConstPtr &msg)
  {
    if (!have_odom_ || !msg || msg->header.frame_id != self_inflation_frame_id_)
    {
      ROS_ERROR("Reference path must be in the local odom frame and body odom must be ready.");
      return;
    }
    if (!msg || msg->poses.empty())
    {
      ROS_WARN_THROTTLE(1.0, "[pathCallback] Received empty /initial_path, ignore.");
      return;
    }

    trigger_ = true;

    std::vector<Eigen::Vector3d> waypoints;
    waypoints.reserve(msg->poses.size());

    for (const auto& pose_stamped : msg->poses)
    {
      Eigen::Vector3d wp;
      wp(0) = pose_stamped.pose.position.x;
      wp(1) = pose_stamped.pose.position.y;
      // Global map height is not body height. Local trajectory uses measured body z.
      wp(2) = odom_pos_(2);
      const Eigen::Vector3d previous = waypoints.empty() ? odom_pos_ : waypoints.back();
      if ((wp - previous).norm() > 0.03)
        waypoints.push_back(wp);
    }
    bool success = planGlobalTrajByWaypoints(waypoints);

    if (success)
    {
      /*** FSM ***/
      if (exec_state_ == WAIT_TARGET)
      {
        changeFSMExecState(GEN_NEW_TRAJ, "TRIG");
      }
      else if (exec_state_ == EXEC_TRAJ)
      {
        changeFSMExecState(REPLAN_TRAJ, "TRIG");
      }

      ROS_INFO("==========================================\n");
    }
    else
    {
      ROS_ERROR("❌ Unable to generate global trajectory!");
    }
  }

  void SCANReplanFSM::odometryCallback(const nav_msgs::OdometryConstPtr &msg)
  {
    odom_pos_(0) = msg->pose.pose.position.x;
    odom_pos_(1) = msg->pose.pose.position.y;
    odom_pos_(2) = msg->pose.pose.position.z;

    if (navi_mode_ == NAVI_MODE::MANUAL_TARGET && !rviz_height_ready_)
    {
      rviz_goal_height_ = odom_pos_(2);
      rviz_height_ready_ = true;
      ROS_INFO("[SCANReplanFSM] Set RViz goal height from initial body_pose z: %.3f", rviz_goal_height_);
    }

    odom_vel_(0) = msg->twist.twist.linear.x;
    odom_vel_(1) = msg->twist.twist.linear.y;
    odom_vel_(2) = msg->twist.twist.linear.z;

    //odom_acc_ = estimateAcc( msg );

    odom_orient_.w() = msg->pose.pose.orientation.w;
    odom_orient_.x() = msg->pose.pose.orientation.x;
    odom_orient_.y() = msg->pose.pose.orientation.y;
    odom_orient_.z() = msg->pose.pose.orientation.z;

    // /leg_odom2 twist is body-frame velocity, SCAN expects odom-frame velocity.
    odom_orient_.normalize();
    odom_vel_ = odom_orient_ * odom_vel_;

    have_odom_ = true;
    recordRecoveryBreadcrumb();
    publishSelfInflationMarker();
  }

  void SCANReplanFSM::go2ExecutionFrozenCallback(const std_msgs::BoolConstPtr &msg)
  {
    go2_execution_frozen_ = msg->data;
  }

  void SCANReplanFSM::updateLocalTrajTimeFreeze()
  {
    const ros::Time now = ros::Time::now();
    double dt = (now - last_freeze_update_time_).toSec();
    last_freeze_update_time_ = now;

    if (dt <= 0.0 || dt > 0.2)
      return;

    LocalTrajData *info = &planner_manager_->local_data_;
    if (go2_execution_frozen_ && info->start_time_.toSec() > 1e-5)
      info->start_time_ += ros::Duration(dt);
  }

  double SCANReplanFSM::getOdomYaw() const
  {
    Eigen::Vector3d heading = odom_orient_.toRotationMatrix().col(0);
    if (heading.head<2>().squaredNorm() < 1e-8)
      return 0.0;
    return std::atan2(heading(1), heading(0));
  }

  double SCANReplanFSM::estimateYawFromSegment(const Eigen::Vector3d &from, const Eigen::Vector3d &to) const
  {
    Eigen::Vector2d diff(to(0) - from(0), to(1) - from(1));
    if (diff.squaredNorm() < 1e-8)
      return getOdomYaw();
    return std::atan2(diff(1), diff(0));
  }

  void SCANReplanFSM::publishRecoveryState()
  {
    std_msgs::Bool msg;
    msg.data = recovery_active_;
    recovery_state_pub_.publish(msg);
  }

  void SCANReplanFSM::resetRecoveryForNewGoal()
  {
    recovery_active_ = false;
    recovery_attempt_count_ = 0;
    recovery_breadcrumb_.clear();
    if (have_odom_)
      recovery_breadcrumb_.push_back(odom_pos_);
    publishRecoveryState();
  }

  void SCANReplanFSM::recordRecoveryBreadcrumb()
  {
    if (!recovery_enabled_ || recovery_active_ || !have_target_)
      return;

    const double record_spacing = std::max(0.05, std::min(0.12, recovery_waypoint_spacing_ * 0.5));
    if (recovery_breadcrumb_.empty() ||
        (odom_pos_.head<2>() - recovery_breadcrumb_.back().head<2>()).norm() >= record_spacing)
    {
      recovery_breadcrumb_.push_back(odom_pos_);
      while (recovery_breadcrumb_.size() > 500)
        recovery_breadcrumb_.pop_front();
    }
  }

  bool SCANReplanFSM::startDeadEndRecovery()
  {
    if (!recovery_enabled_ || recovery_active_ || navi_mode_ != NAVI_MODE::MANUAL_TARGET ||
        recovery_breadcrumb_.size() < 2 || recovery_attempt_count_ >= recovery_max_attempts_)
      return false;

    ++recovery_attempt_count_;
    std::vector<Eigen::Vector3d> recovery_waypoints;
    const auto map = planner_manager_->grid_map_;
    Eigen::Vector3d previous_history = odom_pos_;
    Eigen::Vector3d previous_waypoint = odom_pos_;
    double travelled = 0.0;
    double next_sample = recovery_waypoint_spacing_;

    for (auto it = recovery_breadcrumb_.rbegin(); it != recovery_breadcrumb_.rend(); ++it)
    {
      travelled += (previous_history.head<2>() - it->head<2>()).norm();
      previous_history = *it;
      if (travelled + 1e-6 < next_sample)
        continue;

      Eigen::Vector3d candidate = *it;
      candidate(2) = odom_pos_(2);
      const double candidate_yaw = estimateYawFromSegment(previous_waypoint, candidate);
      if (map && map->getInflateOccupancy(candidate, candidate_yaw) == 0 &&
          (candidate.head<2>() - previous_waypoint.head<2>()).norm() >= 0.08)
      {
        recovery_waypoints.push_back(candidate);
        previous_waypoint = candidate;
        next_sample += recovery_waypoint_spacing_;
      }

      if (travelled >= recovery_distance_)
        break;
    }

    const double exit_distance = recovery_waypoints.empty()
                                     ? 0.0
                                     : (recovery_waypoints.back().head<2>() - odom_pos_.head<2>()).norm();
    if (recovery_waypoints.empty() || exit_distance < std::min(0.35, recovery_distance_ * 0.6))
    {
      ROS_WARN("[dead_end_recovery] attempt %d/%d: insufficient collision-free breadcrumb (%.2fm).",
               recovery_attempt_count_, recovery_max_attempts_, exit_distance);
      return false;
    }

    const Eigen::Vector3d original_goal = end_pt_;
    if (!planGlobalTrajByWaypoints(recovery_waypoints, true))
    {
      end_pt_ = original_goal;
      ROS_WARN("[dead_end_recovery] attempt %d/%d: unable to generate retreat trajectory.",
               recovery_attempt_count_, recovery_max_attempts_);
      return false;
    }

    recovery_saved_goal_ = original_goal;
    recovery_active_ = true;
    replan_fail_count_ = 0;
    publishRecoveryState();
    ROS_WARN("[dead_end_recovery] active: retreat %.2fm through %zu breadcrumb waypoints, then retry original goal.",
             exit_distance, recovery_waypoints.size());
    changeFSMExecState(GEN_NEW_TRAJ, "RECOVERY");
    return true;
  }

  bool SCANReplanFSM::resumeGoalAfterRecovery()
  {
    recovery_active_ = false;
    publishRecoveryState();
    end_pt_ = recovery_saved_goal_;

    const bool success = planner_manager_->planGlobalTraj(
        odom_pos_, Eigen::Vector3d::Zero(), Eigen::Vector3d::Zero(), end_pt_,
        Eigen::Vector3d::Zero(), Eigen::Vector3d::Zero()) &&
                         adjustGlobalTargetIfOccupied();
    if (!success)
    {
      ROS_ERROR("[dead_end_recovery] exited retreat point but failed to restore original goal.");
      return false;
    }

    recovery_breadcrumb_.clear();
    recovery_breadcrumb_.push_back(odom_pos_);
    replan_fail_count_ = 0;
    have_target_ = true;
    have_new_target_ = true;
    visualization_->displayGoalPoint(end_pt_, Eigen::Vector4d(0, 0.5, 0.5, 1), 0.3, 0);
    ROS_WARN("[dead_end_recovery] retreat complete; retry original goal [%.2f, %.2f, %.2f].",
             end_pt_(0), end_pt_(1), end_pt_(2));
    changeFSMExecState(GEN_NEW_TRAJ, "RECOVERY_DONE");
    return true;
  }

  void SCANReplanFSM::publishSelfInflationMarker()
  {
    const double radius = std::max(0.0, self_double_cylinder_radius_);
    const double z_up = std::max(0.0, self_inflation_z_up_);
    const double z_down = std::max(0.0, self_inflation_z_down_);
    const double height = std::max(1e-3, z_up + z_down);

    visualization_msgs::Marker marker;
    marker.header.frame_id = self_inflation_frame_id_.empty() ? "world" : self_inflation_frame_id_;
    marker.header.stamp = ros::Time::now();
    marker.ns = "self_inflation";
    marker.type = visualization_msgs::Marker::CYLINDER;
    marker.action = visualization_msgs::Marker::ADD;
    marker.pose.orientation.w = 1.0;
    marker.scale.x = 2.0 * radius;
    marker.scale.y = 2.0 * radius;
    marker.scale.z = height;
    marker.color.r = 0.1;
    marker.color.g = 0.6;
    marker.color.b = 1.0;
    marker.color.a = 0.4;
    marker.lifetime = ros::Duration(0.2);

    Eigen::Vector3d center = odom_pos_;
    center(2) += 0.5 * (z_up - z_down);

    Eigen::Vector3d heading(std::cos(getOdomYaw()), std::sin(getOdomYaw()), 0.0);
    Eigen::Vector3d front = center + self_double_cylinder_offset_ * heading;
    Eigen::Vector3d rear = center - self_double_cylinder_offset_ * heading;

    marker.id = 0;
    marker.pose.position.x = front(0);
    marker.pose.position.y = front(1);
    marker.pose.position.z = front(2);
    self_inflation_pub_.publish(marker);

    marker.id = 1;
    marker.pose.position.x = rear(0);
    marker.pose.position.y = rear(1);
    marker.pose.position.z = rear(2);
    self_inflation_pub_.publish(marker);
  }

  void SCANReplanFSM::changeFSMExecState(FSM_EXEC_STATE new_state, string pos_call)
  {

    if (new_state == exec_state_)
      continuously_called_times_++;
    else
      continuously_called_times_ = 1;

    static string state_str[7] = {"INIT", "WAIT_TARGET", "GEN_NEW_TRAJ", "REPLAN_TRAJ", "EXEC_TRAJ", "EMERGENCY_STOP"};
    int pre_s = int(exec_state_);
    exec_state_ = new_state;
    if (new_state == EMERGENCY_STOP && navi_mode_ == NAVI_MODE::ROLLING_TARGET)
      beginLocalRecovery(pos_call);
    cout << "[" + pos_call + "]: from " + state_str[pre_s] + " to " + state_str[int(new_state)] << endl;
  }

  std::pair<int, SCANReplanFSM::FSM_EXEC_STATE> SCANReplanFSM::timesOfConsecutiveStateCalls()
  {
    return std::pair<int, FSM_EXEC_STATE>(continuously_called_times_, exec_state_);
  }

  void SCANReplanFSM::printFSMExecState()
  {
    static string state_str[7] = {"INIT", "WAIT_TARGET", "GEN_NEW_TRAJ", "REPLAN_TRAJ", "EXEC_TRAJ", "EMERGENCY_STOP"};

    cout << "[FSM]: state: " + state_str[int(exec_state_)] << endl;
  }

  void SCANReplanFSM::execFSMCallback(const ros::TimerEvent &e)
  {
    updateLocalTrajTimeFreeze();
    if (navi_mode_ == NAVI_MODE::ROLLING_TARGET && (local_hold_ || local_blocked_))
    {
      runLocalRecovery();
      return;
    }

    static int fsm_num = 0;
    fsm_num++;
    if (fsm_num == 100)
    {
      printFSMExecState();
      if (!have_odom_)
        cout << "no odom." << endl;
      if (!trigger_)
        cout << "wait for goal." << endl;
      fsm_num = 0;
    }

    switch (exec_state_)
    {
    case INIT:
    {
      if (!have_odom_)
      {
        return;
      }
      if (!trigger_)
      {
        return;
      }
      changeFSMExecState(WAIT_TARGET, "FSM");
      break;
    }

    case WAIT_TARGET:
    {
      if (!have_target_)
        return;
      else
      {
        changeFSMExecState(GEN_NEW_TRAJ, "FSM");
      }
      break;
    }

    case GEN_NEW_TRAJ:
    {
      setStartStateFromOdomOrCurrentTraj();

      // Eigen::Vector3d rot_x = odom_orient_.toRotationMatrix().block(0, 0, 3, 1);
      // start_yaw_(0)         = atan2(rot_x(1), rot_x(0));
      // start_yaw_(1) = start_yaw_(2) = 0.0;

      bool flag_random_poly_init;
      if (timesOfConsecutiveStateCalls().first == 1)
        flag_random_poly_init = false;
      else
        flag_random_poly_init = true;

      bool success = callReboundReplan(true, flag_random_poly_init);
      if (success)
      {

        replan_fail_count_ = 0;
        changeFSMExecState(EXEC_TRAJ, "FSM");
        flag_escape_emergency_ = true;
      }
      else
      {
        replan_fail_count_++;
        changeFSMExecState(GEN_NEW_TRAJ, "FSM");
      }
      break;
    }

    case REPLAN_TRAJ:
    {

      if (planFromCurrentTraj())
      {
        replan_fail_count_ = 0;
        changeFSMExecState(EXEC_TRAJ, "FSM");
      }
      else
      {
        replan_fail_count_++;
        changeFSMExecState(REPLAN_TRAJ, "FSM");
      }

      break;
    }

    case EXEC_TRAJ:
    {
      /* determine if need to replan */
      LocalTrajData *info = &planner_manager_->local_data_;
      ros::Time time_now = ros::Time::now();
      double t_cur = (time_now - info->start_time_).toSec();
      t_cur = min(info->duration_, t_cur);

      Eigen::Vector3d pos = info->position_traj_.evaluateDeBoorT(t_cur);

      if (recovery_active_)
      {
        const double recovery_error = (end_pt_.head<2>() - odom_pos_.head<2>()).norm();
        if (recovery_error <= recovery_goal_tolerance_)
        {
          if (!resumeGoalAfterRecovery())
            replan_fail_count_ = max_replan_fail_count_;
          break;
        }
        if (t_cur > info->duration_ - 1e-2)
        {
          ROS_WARN("[dead_end_recovery] retreat trajectory ended %.2fm before its target; replan retreat.",
                   recovery_error);
          changeFSMExecState(GEN_NEW_TRAJ, "RECOVERY_CONTINUE");
          break;
        }
      }

      if (isWaypointSequenceMode() &&
          current_wp_ + 1 < (int)active_waypoints_.size() &&
          (end_pt_ - odom_pos_).norm() < 0.5)
      {
        current_wp_++;
        if (planNextWaypoint())
        {
          changeFSMExecState(GEN_NEW_TRAJ, "FSM");
          return;
        }
        replan_fail_count_++;
        changeFSMExecState(GEN_NEW_TRAJ, "FSM");
        return;
      }

      /* && (end_pt_ - pos).norm() < 0.5 */
      if (t_cur > info->duration_ - 1e-2)
      {
        if ((navi_mode_ == NAVI_MODE::REFERENCE_PATH || navi_mode_ == NAVI_MODE::ROLLING_TARGET) &&
            (end_pt_.head<2>() - odom_pos_.head<2>()).norm() > 0.15)
        {
          changeFSMExecState(REPLAN_TRAJ, "REFERENCE_CONTINUE");
          break;
        }
        if (isWaypointSequenceMode() && current_wp_ + 1 < (int)active_waypoints_.size())
        {
          current_wp_++;
          if (planNextWaypoint())
          {
            changeFSMExecState(GEN_NEW_TRAJ, "FSM");
            return;
          }
          replan_fail_count_++;
          changeFSMExecState(GEN_NEW_TRAJ, "FSM");
          return;
        }

        if (isWaypointSequenceMode())
        {
          active_waypoints_.clear();
          current_wp_ = 0;
        }

        have_target_ = false;

        changeFSMExecState(WAIT_TARGET, "FSM");
        return;
      }
      else if ((end_pt_ - pos).norm() < no_replan_thresh_)
      {
        // cout << "near end" << endl;
        return;
      }
      else if ((info->start_pos_ - pos).norm() < replan_thresh_)
      {
        // cout << "near start" << endl;
        return;
      }
      else
      {
        changeFSMExecState(REPLAN_TRAJ, "FSM");
      }
      break;
    }

    case EMERGENCY_STOP:
    {

      if (flag_escape_emergency_) // Avoiding repeated calls
      {
        callEmergencyStop(odom_pos_);
      }
      else
      {
        if (enable_fail_safe_ && !need_hover_stop_ && odom_vel_.norm() < 0.1)
          changeFSMExecState(GEN_NEW_TRAJ, "FSM");
        else if (enable_fail_safe_ && need_hover_stop_ && odom_vel_.norm() < 0.1)
        {
          ROS_INFO("Exiting EMERGENCY_STOP. Switching to WAIT_TARGET. Need a new target point.");
          need_hover_stop_ = false;
          have_target_ = false;
          trigger_ = false;
          changeFSMExecState(WAIT_TARGET, "EMERGENCY_EXIT");
        }
      }

      flag_escape_emergency_ = false;
      break;
    }
    }

    finishProcess();

    data_disp_.header.stamp = ros::Time::now();
    data_disp_pub_.publish(data_disp_);
  }

  void SCANReplanFSM::finishProcess()
  {
    if (recovery_enabled_ && !recovery_active_ &&
        replan_fail_count_ >= recovery_trigger_fail_count_ &&
        recovery_attempt_count_ < recovery_max_attempts_)
    {
      if (startDeadEndRecovery())
        return;
    }

    if (replan_fail_count_ >= max_replan_fail_count_)
    {
      ROS_WARN("Replan failed %d times. Emergency stop and wait for a new target.", replan_fail_count_);
      replan_fail_count_ = 0;
      need_hover_stop_ = true;
      recovery_active_ = false;
      publishRecoveryState();
      flag_escape_emergency_ = true;
      changeFSMExecState(EMERGENCY_STOP, "finishProcess");
    }
  }

  bool SCANReplanFSM::planFromCurrentTraj()
  {
    LocalTrajData *info = &planner_manager_->local_data_;
    ros::Time time_now = ros::Time::now();
    double t_cur = (time_now - info->start_time_).toSec();
    t_cur = std::min(std::max(t_cur, 0.0), info->duration_);

    //cout << "info->velocity_traj_=" << info->velocity_traj_.get_control_points() << endl;

    start_pt_ = odom_pos_;
    start_vel_ = info->velocity_traj_.evaluateDeBoorT(t_cur);
    start_acc_ = info->acceleration_traj_.evaluateDeBoorT(t_cur);

    const Eigen::Vector2d to_goal = end_pt_.head<2>() - odom_pos_.head<2>();
    if (to_goal.norm() > 1e-3 && start_vel_.head<2>().dot(to_goal) < 0.0)
    {
      start_vel_.setZero();
      start_acc_.setZero();
    }

    // Preserve the Dijkstra reference and its progress across local replans.
    // The original implementation replaced it by a straight line to the goal.
    if (navi_mode_ != NAVI_MODE::REFERENCE_PATH && !planner_manager_->planGlobalTraj(
            start_pt_,
            start_vel_,
            start_acc_,
            end_pt_,
            Eigen::Vector3d::Zero(),
            Eigen::Vector3d::Zero()))
    {
      ROS_ERROR("[navi_mode=%d] Unable to refresh global trajectory from odom to current target.", navi_mode_);
      return false;
    }

    if (navi_mode_ != NAVI_MODE::REFERENCE_PATH && navi_mode_ != NAVI_MODE::ROLLING_TARGET && !adjustGlobalTargetIfOccupied())
      return false;

    bool success = callReboundReplan(true, false);
    if (!success)
    {
      success = callReboundReplan(true, true);
      if (!success)
        return false;
    }

    return true;
  }

  void SCANReplanFSM::setStartStateFromOdomOrCurrentTraj()
  {
    start_pt_ = odom_pos_;
    start_vel_ = odom_vel_;
    start_acc_.setZero();

    LocalTrajData *info = &planner_manager_->local_data_;
    if (info->start_time_.toSec() < 1e-5 || info->duration_ <= 1e-5)
      return;

    const double raw_t_cur = (ros::Time::now() - info->start_time_).toSec();
    if (raw_t_cur < -1e-3 || raw_t_cur > info->duration_ + 0.2)
      return;

    const double t_cur = std::min(std::max(raw_t_cur, 0.0), info->duration_);
    start_vel_ = info->velocity_traj_.evaluateDeBoorT(t_cur);
    start_acc_ = info->acceleration_traj_.evaluateDeBoorT(t_cur);

    const Eigen::Vector2d to_goal = end_pt_.head<2>() - odom_pos_.head<2>();
    if (to_goal.norm() > 1e-3 && start_vel_.head<2>().dot(to_goal) < 0.0)
    {
      start_vel_.setZero();
      start_acc_.setZero();
    }
  }

  void SCANReplanFSM::checkCollisionCallback(const ros::TimerEvent &e)
  {
    updateLocalTrajTimeFreeze();
    if (navi_mode_ == NAVI_MODE::ROLLING_TARGET && (local_hold_ || local_blocked_))
      return;

    LocalTrajData *info = &planner_manager_->local_data_;
    auto map = planner_manager_->grid_map_;

    if (exec_state_ == WAIT_TARGET || info->start_time_.toSec() < 1e-5)
      return;

    /* ---------- check trajectory ---------- */
    constexpr double time_step = 0.01;
    double t_cur = (ros::Time::now() - info->start_time_).toSec();
    double t_2_3 = info->duration_ * 2 / 3;
    for (double t = t_cur; t < info->duration_; t += time_step)
    {
      if (t_cur < t_2_3 && t >= t_2_3) // If t_cur < t_2_3, only the first 2/3 partition of the trajectory is considered valid and will get checked.
        break;

      Eigen::Vector3d pos = info->position_traj_.evaluateDeBoorT(t);
      Eigen::Vector3d pos_next = info->position_traj_.evaluateDeBoorT(std::min(t + time_step, info->duration_));
      if (map->getInflateOccupancy(pos, estimateYawFromSegment(pos, pos_next)))
      {
        if (navi_mode_ == NAVI_MODE::ROLLING_TARGET && t-t_cur < emergency_time_)
        {
          beginLocalRecovery("Near-term trajectory collision");
          changeFSMExecState(EMERGENCY_STOP,"SAFETY");
          return;
        }
        if (planFromCurrentTraj()) // Make a chance
        {
          changeFSMExecState(EXEC_TRAJ, "SAFETY");
          return;
        }
        else
        {
          if (t - t_cur < emergency_time_) // 0.8s of emergency time
          {
            ROS_WARN("Suddenly discovered obstacles. emergency stop! time=%f", t - t_cur);
            changeFSMExecState(EMERGENCY_STOP, "SAFETY");
          }
          else
          {
            //ROS_WARN("current traj in collision, replan.");
            changeFSMExecState(REPLAN_TRAJ, "SAFETY");
          }
          return;
        }
        break;
      }
    }
  }

  bool SCANReplanFSM::callReboundReplan(bool flag_use_poly_init, bool flag_randomPolyTraj)
  {

    getLocalTarget();

    bool plan_success =
        planner_manager_->reboundReplan(start_pt_, start_vel_, start_acc_, local_target_pt_, local_target_vel_, (have_new_target_ || flag_use_poly_init), flag_randomPolyTraj);
    have_new_target_ = false;

    cout << "final_plan_success=" << plan_success << endl;

    if (plan_success && navi_mode_ == NAVI_MODE::ROLLING_TARGET)
    {
      plan_success = validateLocalTrajectory();
      if (!plan_success)
        beginLocalRecovery("Candidate trajectory/initial turn blocked");
    }

    if (plan_success)
    {
      local_hold_ = local_blocked_ = false;
      checked_trajectory_ = true;
      local_reason_ = "Checked trajectory ready";

      auto info = &planner_manager_->local_data_;

      /* publish traj */
      scan_planner::Bspline bspline;
      bspline.order = 3;
      bspline.start_time = info->start_time_;
      bspline.traj_id = info->traj_id_;

      Eigen::MatrixXd pos_pts = info->position_traj_.getControlPoint();
      bspline.pos_pts.reserve(pos_pts.cols());
      for (int i = 0; i < pos_pts.cols(); ++i)
      {
        geometry_msgs::Point pt;
        pt.x = pos_pts(0, i);
        pt.y = pos_pts(1, i);
        pt.z = pos_pts(2, i);
        bspline.pos_pts.push_back(pt);
      }

      Eigen::VectorXd knots = info->position_traj_.getKnot();
      bspline.knots.reserve(knots.rows());
      for (int i = 0; i < knots.rows(); ++i)
      {
        bspline.knots.push_back(knots(i));
      }

      bspline_pub_.publish(bspline);
      publishTaggedTrajectory(bspline);
      publishPlannerState();

      visualization_->displayOptimalTraj(info->position_traj_, 0);
    }

    return plan_success;
  }

  bool SCANReplanFSM::callEmergencyStop(Eigen::Vector3d stop_pos)
  {

    planner_manager_->EmergencyStop(stop_pos);

    auto info = &planner_manager_->local_data_;

    /* publish traj */
    scan_planner::Bspline bspline;
    bspline.order = 3;
    bspline.start_time = info->start_time_;
    bspline.traj_id = info->traj_id_;

    Eigen::MatrixXd pos_pts = info->position_traj_.getControlPoint();
    bspline.pos_pts.reserve(pos_pts.cols());
    for (int i = 0; i < pos_pts.cols(); ++i)
    {
      geometry_msgs::Point pt;
      pt.x = pos_pts(0, i);
      pt.y = pos_pts(1, i);
      pt.z = pos_pts(2, i);
      bspline.pos_pts.push_back(pt);
    }

    Eigen::VectorXd knots = info->position_traj_.getKnot();
    bspline.knots.reserve(knots.rows());
    for (int i = 0; i < knots.rows(); ++i)
    {
      bspline.knots.push_back(knots(i));
    }

    bspline_pub_.publish(bspline);
    publishTaggedTrajectory(bspline);

    return true;
  }

  void SCANReplanFSM::getLocalTarget()
  {
    double t;

    double t_step = planning_horizon_ / 20 / planner_manager_->pp_.max_vel_;
    double dist_min = 9999, dist_min_t = 0.0;
    double target_t = planner_manager_->global_data_.global_duration_;
    for (t = planner_manager_->global_data_.last_progress_time_; t < planner_manager_->global_data_.global_duration_; t += t_step)
    {
      Eigen::Vector3d pos_t = planner_manager_->global_data_.getPosition(t);
      double dist = (pos_t - start_pt_).norm();

      if (t < planner_manager_->global_data_.last_progress_time_ + 1e-5 && dist > planning_horizon_)
      {
        ROS_ERROR_STREAM("[getLocalTarget] last_progress_time mismatch: "
                         << "dist_to_progress_pt=" << dist
                         << ", planning_horizon=" << planning_horizon_
                         << ", last_progress_time=" << planner_manager_->global_data_.last_progress_time_);
        local_target_pt_ = pos_t;
        target_t = t;
        planner_manager_->global_data_.last_progress_time_ = t;
        break;
      }
      if (dist < dist_min)
      {
        dist_min = dist;
        dist_min_t = t;
      }
      if (dist >= planning_horizon_)
      {
        local_target_pt_ = pos_t;
        target_t = t;
        planner_manager_->global_data_.last_progress_time_ = dist_min_t;
        break;
      }
    }
    if (t >= planner_manager_->global_data_.global_duration_) // Last global point
    {
      local_target_pt_ = end_pt_;
      target_t = planner_manager_->global_data_.global_duration_;
    }

    auto targetOccupancy = [&](const Eigen::Vector3d &pt) {
      return planner_manager_->grid_map_->getInflateOccupancy(pt, estimateYawFromSegment(odom_pos_, pt));
    };

    if (targetOccupancy(local_target_pt_) != 0)
    {
      bool found_free_target = false;
      double adjusted_t = target_t;

      for (double dt = 0.0; dt <= planner_manager_->global_data_.global_duration_; dt += t_step)
      {
        double t_forward = target_t + dt;
        if (t_forward <= planner_manager_->global_data_.global_duration_)
        {
          Eigen::Vector3d pt = planner_manager_->global_data_.getPosition(t_forward);
          if (targetOccupancy(pt) == 0)
          {
            local_target_pt_ = pt;
            adjusted_t = t_forward;
            found_free_target = true;
            break;
          }
        }

        double t_backward = target_t - dt;
        if (t_backward >= std::max(0.0, dist_min_t))
        {
          Eigen::Vector3d pt = planner_manager_->global_data_.getPosition(t_backward);
          if (targetOccupancy(pt) == 0)
          {
            local_target_pt_ = pt;
            adjusted_t = t_backward;
            found_free_target = true;
            break;
          }
        }
      }

      if (found_free_target)
      {
        ROS_WARN_THROTTLE(1.0, "Local target in collision, adjusted to a nearby collision-free point.");
        target_t = adjusted_t;
      }
      else
      {
        ROS_WARN_THROTTLE(1.0, "Local target in collision and no nearby collision-free target was found.");
      }
    }

    if ((end_pt_ - local_target_pt_).norm() < (planner_manager_->pp_.max_vel_ * planner_manager_->pp_.max_vel_) / (2 * planner_manager_->pp_.max_acc_))
    {
      // local_target_vel_ = (end_pt_ - init_pt_).normalized() * planner_manager_->pp_.max_vel_ * (( end_pt_ - local_target_pt_ ).norm() / ((planner_manager_->pp_.max_vel_*planner_manager_->pp_.max_vel_)/(2*planner_manager_->pp_.max_acc_)));
      // cout << "A" << endl;
      local_target_vel_ = Eigen::Vector3d::Zero();
    }
    else
    {
      local_target_vel_ = planner_manager_->global_data_.getVelocity(target_t);
      // cout << "AA" << endl;
    }
  }

  bool SCANReplanFSM::resetCallback(std_srvs::Trigger::Request &, std_srvs::Trigger::Response &res)
  {
    ++execution_generation_;
    local_hold_ = local_blocked_ = checked_trajectory_ = false;
    local_attempts_ = 0;
    local_reason_ = "Task reset";
    target_accept_after_ = ros::Time::now();
    have_target_ = have_new_target_ = trigger_ = false;
    replan_fail_count_ = 0;
    need_hover_stop_ = false;
    active_waypoints_.clear();
    resetRecoveryForNewGoal();
    planner_manager_->local_data_.start_time_ = ros::Time(0);
    planner_manager_->local_data_.duration_ = 0;
    changeFSMExecState(WAIT_TARGET, "RESET");
    publishPlannerState();
    res.success = true;
    res.message = "SCAN task cleared";
    return true;
  }

  bool SCANReplanFSM::checkPosesCallback(scan_map_navigation::CheckPoses::Request &req,
                                        scan_map_navigation::CheckPoses::Response &res)
  {
    res.safe = false;
    if (!have_odom_ || req.samples.header.frame_id != self_inflation_frame_id_ || req.samples.poses.empty())
    { res.message = "Missing odom, invalid frame or empty samples"; return true; }
    for (const auto &p : req.samples.poses)
    {
      Eigen::Vector3d v(p.position.x, p.position.y, p.position.z);
      Eigen::Quaterniond q(p.orientation.w, p.orientation.x, p.orientation.y, p.orientation.z);
      if (!v.allFinite() || !q.coeffs().allFinite() || q.norm() < 0.1)
      { res.message = "Invalid pose"; return true; }
      q.normalize();
      double yaw = std::atan2(2*(q.w()*q.z()+q.x()*q.y()), 1-2*(q.y()*q.y()+q.z()*q.z()));
      if (planner_manager_->grid_map_->getInflateOccupancy(v, yaw) != 0)
      { res.message = "Local footprint occupied or outside sliding map"; return true; }
    }
    res.safe = true;
    return true;
  }
} // namespace scan_planner
