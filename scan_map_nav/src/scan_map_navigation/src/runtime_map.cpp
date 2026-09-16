#include <scan_map_navigation/evidence_grid.h>
#include <scan_map_navigation/PlanningGrid.h>
#include <hdl_localization/ScanMatchingStatus.h>
#include <nav_msgs/OccupancyGrid.h>
#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/point_cloud2_iterator.h>
#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <deque>

namespace sn=scan_map_navigation;
class RuntimeMap {
  ros::NodeHandle nh_{"~"};
  tf::TransformListener tf_;
  ros::Subscriber map_sub_,cloud_sub_,status_sub_;
  ros::WallTimer retry_timer_;
  ros::Publisher output_,display_;
  sn::EvidenceGrid grid_;
  sn::PlanningGrid message_;
  hdl_localization::ScanMatchingStatus status_;
  ros::WallTime status_received_;
  ros::Time last_cloud_;
  tf::StampedTransform last_map_odom_;
  bool have_transform_=false, have_map_=false;
  int max_rays_=4096;
  double period_=.2;
  double ground_height_=0,ground_margin_=.03;
  struct PendingCloud {
    sensor_msgs::PointCloud2::ConstPtr cloud;
    ros::WallTime received;
  };
  std::deque<PendingCloud> pending_;
  size_t pending_bytes_=0;
  static constexpr size_t max_pending_clouds_=8;
  static constexpr size_t max_pending_bytes_=16*1024*1024;
  void clearPending() { pending_.clear(); pending_bytes_=0; }
  void popPending() {
    pending_bytes_-=pending_.front().cloud->data.size(); pending_.pop_front();
  }
  void invalid(const std::string& reason) {
    clearPending(); // do not replay observations from before a quality/map fault
    if (have_map_) { message_.valid=false; output_.publish(message_); }
    ROS_WARN_THROTTLE(2.0,"Runtime map not current: %s",reason.c_str());
  }
  bool quality(const ros::Time& stamp) const {
    return (ros::WallTime::now()-status_received_).toSec() <= .7 &&
      std::abs((stamp-status_.header.stamp).toSec()) <= .7 && status_.has_converged &&
      std::isfinite(status_.matching_error) && status_.matching_error <= .3 &&
      std::isfinite(status_.inlier_fraction) && status_.inlier_fraction >= .5;
  }
public:
  RuntimeMap() {
    nh_.param("max_rays",max_rays_,4096);
    nh_.param("update_period",period_,.2);
    nh_.param("hit_frames",grid_.cfg.hit_frames,2);
    nh_.param("free_frames",grid_.cfg.free_frames,4);
    nh_.param("free_duration",grid_.cfg.free_duration,.6);
    nh_.param("free_override_ttl",grid_.cfg.free_ttl,5.0);
    nh_.param("ground_height",ground_height_,0.0);
    nh_.param("ground_margin",ground_margin_,.03);
    if (max_rays_<64 || !std::isfinite(period_) || period_<=0 || period_>.3 || grid_.cfg.hit_frames<2 ||
        grid_.cfg.free_frames<3 || !std::isfinite(grid_.cfg.free_duration) || grid_.cfg.free_duration<.4 ||
        !std::isfinite(grid_.cfg.free_ttl) || grid_.cfg.free_ttl<=0 ||
        !std::isfinite(ground_height_+ground_margin_) || ground_margin_<0 || ground_margin_>.05)
      throw std::invalid_argument("Invalid runtime-map evidence parameters");
    output_=nh_.advertise<sn::PlanningGrid>("/scan_map_nav/runtime_grid",1,true);
    display_=nh_.advertise<nav_msgs::OccupancyGrid>("/scan_map_nav/runtime_map",1,true);
    map_sub_=nh_.subscribe<nav_msgs::OccupancyGrid>("/map",1,[this](const nav_msgs::OccupancyGrid::ConstPtr& m) {
      const auto& q=m->info.origin.orientation;
      if (m->header.frame_id!="map" || !std::isfinite(m->info.origin.position.x+m->info.origin.position.y) ||
          !std::isfinite(q.x+q.y+q.z+q.w) ||
          std::abs(q.x)+std::abs(q.y)+std::abs(q.z)>1e-6 || std::abs(q.w-1)>1e-6) {
        invalid("Prior must be an axis-aligned map grid"); return;
      }
      if (have_map_ && grid_.prior==m->data && message_.info==m->info) return;
      try { grid_.reset(m->info.width,m->info.height,m->info.resolution,
                       m->info.origin.position.x,m->info.origin.position.y,m->data); }
      catch (const std::exception& e) { invalid(e.what()); return; }
      have_map_=true; message_.info=m->info; message_.header.frame_id="map";
      message_.occupancy=message_.topology=m->data; ++message_.revision;
      invalid("Waiting for valid timestamped lidar observation");
    });
    status_sub_=nh_.subscribe<hdl_localization::ScanMatchingStatus>("/status",1,
      [this](const hdl_localization::ScanMatchingStatus::ConstPtr& m) {
        status_=*m; status_received_=ros::WallTime::now();
        if (!quality(ros::Time::now())) invalid("NDT quality/stamp rejected");
    });
    cloud_sub_=nh_.subscribe("/rslidar_points",1,&RuntimeMap::cloud,this);
    retry_timer_=nh_.createWallTimer(ros::WallDuration(.01),&RuntimeMap::retryPending,this);
  }
  void cloud(const sensor_msgs::PointCloud2::ConstPtr& m) {
    if (!have_map_) return;
    const double age=(ros::Time::now()-m->header.stamp).toSec();
    if (age<-.2 || age>.7 || m->header.stamp.toSec()<=0) {
      invalid("Stale cloud"); return;
    }
    if (m->header.stamp<=last_cloud_) return; // no duplicate frames as clearing votes
    if ((m->header.stamp-last_cloud_).toSec()<period_-1e-3) return;
    if (m->data.empty() || m->data.size()>max_pending_bytes_) {
      invalid("Empty/oversized cloud cannot enter TF wait queue"); return;
    }
    // Keep arrival callbacks short so delayed NDT status can also be received.
    // Newer untransformable frames MUST NOT replace every older waiting frame.
    if (std::any_of(pending_.begin(),pending_.end(),[&](const PendingCloud& p) {
          return p.cloud->header.stamp==m->header.stamp; })) return;
    while (!pending_.empty() && (pending_.size()>=max_pending_clouds_ ||
           pending_bytes_+m->data.size()>max_pending_bytes_)) popPending();
    const PendingCloud entry{m,ros::WallTime::now()};
    auto it=std::upper_bound(pending_.begin(),pending_.end(),m->header.stamp,
        [](const ros::Time& stamp,const PendingCloud& p) { return stamp<p.cloud->header.stamp; });
    pending_.insert(it,entry); pending_bytes_+=m->data.size();
  }
  void retryPending(const ros::WallTimerEvent&) {
    if (pending_.empty()) return;
    const auto now=ros::Time::now();
    const auto wall=ros::WallTime::now();
    for (auto it=pending_.begin();it!=pending_.end();) {
      const auto stamp=it->cloud->header.stamp;
      const double age=(now-stamp).toSec();
      if (age<-.2 || age>.7 || (wall-it->received).toSec()>.7 ||
          stamp<=last_cloud_ || (stamp-last_cloud_).toSec()<period_-1e-3) {
        pending_bytes_-=it->cloud->data.size(); it=pending_.erase(it);
      } else ++it;
    }
    if (pending_.empty()) return;
    if (!quality(now)) { invalid("NDT quality/stamp rejected while waiting for TF"); return; }
    // Process the newest READY observation, not the newest received one. This
    // avoids both head-of-line blocking and accumulating an old-frame backlog.
    for (auto it=pending_.rbegin();it!=pending_.rend();++it) {
      const auto stamp=it->cloud->header.stamp;
      const auto& sensor=it->cloud->header.frame_id;
      if (!tf_.canTransform("map",sensor,stamp) || !tf_.canTransform("odom",sensor,stamp) ||
          !tf_.canTransform("base_link",sensor,stamp) || !tf_.canTransform("odom","base_link",stamp) ||
          !tf_.canTransform("map","base_link",stamp) || !tf_.canTransform("map","odom",stamp)) continue;
      const PendingCloud ready=*it;
      while (!pending_.empty() && pending_.front().cloud->header.stamp<=stamp) popPending();
      processCloud(ready);
      return;
    }
    ROS_WARN_THROTTLE(2.0,"Runtime map waiting for exact cloud-stamp TF; pending=%zu, oldest age=%.3fs (limit 0.7s)",
                      pending_.size(),(now-pending_.front().cloud->header.stamp).toSec());
    // No fabricated timestamp/publication to make an old map look fresh.
  }
  void processCloud(const PendingCloud& entry) {
    const auto& m=entry.cloud;
    if (!quality(m->header.stamp)) { invalid("Unreliable localization for queued cloud"); return; }
    try {
      tf::StampedTransform map_sensor,odom_sensor,body_sensor,odom_body,map_body,map_odom;
      const auto stamp=m->header.stamp;
      tf_.lookupTransform("map",m->header.frame_id,stamp,map_sensor);
      tf_.lookupTransform("odom",m->header.frame_id,stamp,odom_sensor);
      tf_.lookupTransform("base_link",m->header.frame_id,stamp,body_sensor);
      tf_.lookupTransform("odom","base_link",stamp,odom_body);
      tf_.lookupTransform("map","base_link",stamp,map_body);
      tf_.lookupTransform("map","odom",stamp,map_odom);
      const auto body=map_body.getOrigin();
      if (have_transform_) {
        // Evaluate correction at current body position, not the world origin.
        const auto op=odom_body.getOrigin();
        const double shift=((map_odom*op)-(last_map_odom_*op)).length();
        const double yaw=std::abs(std::atan2(std::sin(tf::getYaw(map_odom.getRotation())-
            tf::getYaw(last_map_odom_.getRotation())),std::cos(tf::getYaw(map_odom.getRotation())-
            tf::getYaw(last_map_odom_.getRotation()))));
        if (shift>.8 || yaw>.5) {
          grid_.forget(); last_map_odom_=map_odom;
          grid_.snapshot(stamp.toSec(),message_.occupancy,message_.topology);
          ++message_.revision; invalid("Localization jumped; runtime evidence discarded"); return;
        }
      }
      last_map_odom_=map_odom; have_transform_=true;
      const size_t count=size_t(m->width)*m->height;
      if (!count || count>1000000 || m->is_bigendian || size_t(m->row_step)!=size_t(m->width)*m->point_step ||
          m->data.size()<size_t(m->row_step)*m->height) { invalid("Empty/truncated/unsupported cloud"); return; }
      for (const std::string axis:{"x","y","z"}) {
        auto it=std::find_if(m->fields.begin(),m->fields.end(),[&](const sensor_msgs::PointField& f){return f.name==axis;});
        if (it==m->fields.end() || it->datatype!=sensor_msgs::PointField::FLOAT32 || it->count!=1 ||
            it->offset+sizeof(float)>m->point_step) { invalid("Invalid XYZ fields"); return; }
      }
      sensor_msgs::PointCloud2ConstIterator<float> px(*m,"x"),py(*m,"y"),pz(*m,"z");
      const size_t stride=std::max(size_t(1),(count+max_rays_-1)/max_rays_);
      const double body_z=odom_body.getOrigin().z();
      const auto origin=map_sensor.getOrigin();
      const sn::Point3 start{origin.x(),origin.y(),odom_sensor.getOrigin().z()-body_z};
      std::vector<sn::Ray> rays;
      rays.reserve(std::min(count,size_t(max_rays_)));
      for (size_t i=0;i<count;++i,++px,++py,++pz) {
        if (i%stride) continue;
        const tf::Vector3 p(*px,*py,*pz);
        if (!std::isfinite(p.x()+p.y()+p.z()) || p.length()<.15 || p.length()>4.0) continue;
        const auto b=body_sensor*p;
        if (std::abs(b.x())<=.53 && std::abs(b.y())<=.35 && b.z()>=-.25 && b.z()<=.20) continue;
        const auto map=map_sensor*p, odom=odom_sensor*p;
        if (!std::isfinite(map.x()+map.y()+odom.z())) continue;
        // Ground returns remain useful finite ray endpoints, but are never
        // marked as obstacles, including when the body height changes.
        rays.push_back({start,{map.x(),map.y(),odom.z()-body_z},odom.z()>ground_height_+ground_margin_});
      }
      if (rays.empty()) { invalid("No valid lidar returns"); return; }
      if ((ros::Time::now()-stamp).toSec()>.7 || (ros::WallTime::now()-entry.received).toSec()>.7) {
        invalid("Cloud expired before evidence update"); return;
      }
      last_cloud_=stamp;
      grid_.observe(rays,stamp.toSec(),body.x(),body.y(),tf::getYaw(map_body.getRotation()));
      grid_.snapshot(stamp.toSec(),message_.occupancy,message_.topology);
      message_.header.stamp=stamp; message_.header.seq=++message_.revision; message_.valid=true;
      output_.publish(message_);
      nav_msgs::OccupancyGrid display;
      display.header=message_.header; display.info=message_.info; display.data=message_.occupancy;
      display_.publish(display);
    } catch (const tf::TransformException& e) {
      ROS_WARN_THROTTLE(2.0,"Runtime map waiting for timestamped TF: %s",e.what());
      // No evidence is added; the existing sensor-time freshness guard remains.
    } catch (const std::exception& e) { invalid(e.what()); }
  }
};
int main(int argc,char** argv) {
  ros::init(argc,argv,"scan_runtime_map");
  RuntimeMap runtime;
  ros::spin();
}
