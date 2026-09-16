#pragma once
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <limits>
#include <stdexcept>
#include <unordered_map>
#include <vector>

namespace scan_map_navigation {
struct Point3 { double x, y, z; }; // XY in map; Z relative to odom body height
struct Ray { Point3 origin, end; bool mark=true; };

// Sensor-independent, bounded storage. Unknown/missing observations NEVER clear.
class EvidenceGrid {
public:
  struct Config {
    int hit_frames = 2, free_frames = 4, height_bins = 3;
    double hit_duration = .15, free_duration = .6, evidence_gap = .5;
    double z_min = -.25, z_max = .20, free_ttl = 5.0, endpoint_margin = .10;
  } cfg;
  struct Evidence {
    int override_value = -1, hit_count = 0, free_count = 0;
    double hit_start = 0, last_hit = -1e9, free_start = 0, last_free = -1e9;
    double free_validated = -1e9;
  };
  int width = 0, height = 0;
  double resolution = .05, origin_x = 0, origin_y = 0;
  std::vector<int8_t> prior;
  std::vector<Evidence> evidence;
  double last_observation=-1e9;

  void reset(int w, int h, double r, double x, double y, const std::vector<int8_t>& data) {
    if (w <= 0 || h <= 0 || !std::isfinite(r) || r <= 0 || data.size() != size_t(w)*h ||
        data.size() > 4000000 || cfg.height_bins < 1 || cfg.height_bins > 8)
      throw std::invalid_argument("Invalid runtime grid geometry");
    width=w; height=h; resolution=r; origin_x=x; origin_y=y;
    prior=data; forget();
  }
  int index(double x, double y) const {
    const int ix=std::floor((x-origin_x)/resolution), iy=std::floor((y-origin_y)/resolution);
    return ix >= 0 && iy >= 0 && ix < width && iy < height ? iy*width+ix : -1;
  }
  void forget() { evidence.assign(prior.size(), Evidence()); last_observation=-1e9; }

  // One frame contributes at most ONE vote per cell. Hit wins over every free ray.
  // Require all vertical bands in EACH confirming frame, not a single high beam
  // projected through a low box. Endpoints and a guard margin are never cleared.
  void observe(const std::vector<Ray>& rays, double now, double body_x, double body_y, double body_yaw) {
    if (!std::isfinite(now) || now<=last_observation) return;
    last_observation=now;
    struct Frame { bool hit=false; unsigned mask=0; };
    std::unordered_map<int, Frame> frame;
    const unsigned all=(1u<<cfg.height_bins)-1;
    const double c=std::cos(body_yaw), s=std::sin(body_yaw);
    auto self = [&](double x, double y) {
      const double dx=x-body_x, dy=y-body_y;
      // Never infer the space hidden by the robot itself to be empty.
      return std::abs(c*dx+s*dy) <= .53+resolution && std::abs(-s*dx+c*dy) <= .35+resolution;
    };
    for (const auto& ray:rays) {
      const auto& a=ray.origin; const auto& b=ray.end;
      if (!std::isfinite(a.x+a.y+a.z+b.x+b.y+b.z)) continue;
      const double dx=b.x-a.x, dy=b.y-a.y, dz=b.z-a.z;
      const double len=std::sqrt(dx*dx+dy*dy+dz*dz);
      if (len < .15 || len > 4.0) continue;
      const int end=index(b.x,b.y);
      if (ray.mark && end >= 0 && !self(b.x,b.y) && b.z >= cfg.z_min && b.z <= cfg.z_max)
        frame[end].hit=true;
      const int steps=std::max(1,int(std::ceil(len/(resolution*.5))));
      for (int k=1;k<steps;++k) {
        const double u=double(k)/steps;
        if ((1-u)*len < cfg.endpoint_margin) break;
        const double x=a.x+u*dx, y=a.y+u*dy, z=a.z+u*dz;
        if (z < cfg.z_min || z >= cfg.z_max || self(x,y)) continue;
        const int cell=index(x,y);
        if (cell < 0) continue;
        const int band=std::min(cfg.height_bins-1,int((z-cfg.z_min)/(cfg.z_max-cfg.z_min)*cfg.height_bins));
        frame[cell].mask |= 1u<<band;
      }
    }
    for (const auto& entry:frame) {
      auto& e=evidence[entry.first]; const auto& f=entry.second;
      if (f.hit) {
        e.free_count=0; e.last_free=-1e9;
        // A new occupied observation immediately revokes a previous free override.
        // Confirmation is still needed before inserting a NEW obstacle into prior free space.
        if (e.override_value == 0) e.override_value=-1;
        if (now-e.last_hit > cfg.evidence_gap) { e.hit_count=0; e.hit_start=now; }
        e.last_hit=now; ++e.hit_count;
        if (e.hit_count >= cfg.hit_frames && now-e.hit_start >= cfg.hit_duration)
          e.override_value=100;
      } else if (f.mask == all) {
        e.hit_count=0; e.last_hit=-1e9;
        if (now-e.last_free > cfg.evidence_gap) { e.free_count=0; e.free_start=now; }
        e.last_free=now; ++e.free_count;
        if (e.free_count >= cfg.free_frames && now-e.free_start >= cfg.free_duration) {
          e.override_value=0; e.free_validated=now;
        }
      } else {
        // Partial-height returns are NOT a confirmation; break clearing streak.
        e.free_count=0; e.last_free=-1e9;
      }
    }
    for (auto& e:evidence) {
      if (e.last_free!=now) { e.free_count=0; e.last_free=-1e9; }
      if (e.last_hit!=now) { e.hit_count=0; e.last_hit=-1e9; }
    }
  }
  void snapshot(double now, std::vector<int8_t>& occupancy, std::vector<int8_t>& topology) const {
    occupancy=topology=prior;
    for (size_t i=0;i<prior.size();++i) {
      const auto& e=evidence[i];
      if (e.override_value == 100) occupancy[i]=100; // no age-to-free conversion
      else if (e.override_value == 0 && now-e.free_validated <= cfg.free_ttl) {
        occupancy[i]=0; topology[i]=0;
      }
      // An expired clear override falls BACK to the prior, never to free.
    }
  }
};

// Same ROS inflation cost law and dimensions as the original configuration.
// Rebuilt from corrected occupancy each time, so removed obstacles leave no halo.
inline std::vector<uint8_t> inflate(const std::vector<int8_t>& cells, int w, int h,
                                  double resolution, double radius=.65, double inscribed=.35, double scale=5) {
  std::vector<uint8_t> out(cells.size());
  for (size_t i=0;i<cells.size();++i) out[i]=cells[i]<0 ? 255 : cells[i]>=65 ? 254 : 0;
  struct Offset { int x,y; uint8_t cost; };
  std::vector<Offset> offsets;
  const int n=std::ceil(radius/resolution);
  for (int y=-n;y<=n;++y) for (int x=-n;x<=n;++x) {
    const double d=std::hypot(x,y)*resolution;
    // ROS InflationLayer rounds its radius UP to whole cells before enqueueing.
    if (std::hypot(x,y)>n+1e-9) continue;
    const uint8_t cost = !x && !y ? 254 : d<=inscribed ? 253 : uint8_t(252*std::exp(-scale*(d-inscribed)));
    offsets.push_back({x,y,cost});
  }
  for (int y=0;y<h;++y) for (int x=0;x<w;++x) if (cells[y*w+x]>=65)
    for (const auto& o:offsets) {
      const int xx=x+o.x, yy=y+o.y;
      if (xx<0 || yy<0 || xx>=w || yy>=h) continue;
      auto& v=out[yy*w+xx];
      if (v!=255) v=std::max(v,o.cost); // unknown remains non-traversable
    }
  return out;
}
} // namespace scan_map_navigation
