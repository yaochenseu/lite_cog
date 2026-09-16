#include <scan_map_navigation/evidence_grid.h>
#include <cassert>
#include <iostream>
using namespace scan_map_navigation;

EvidenceGrid grid(int8_t prior=100) {
  EvidenceGrid g;
  std::vector<int8_t> cells(1600,0);
  cells[20*40+30]=prior; // (1.05,.05)
  cells[30*40+30]=100; // unobserved wall
  g.reset(40,40,.1,-2,-2,cells);
  return g;
}
std::vector<Ray> clearRays(int mask=7) {
  std::vector<Ray> rays;
  for (int bin=0;bin<3;++bin) if (mask&(1<<bin)) {
    const double z=-.25+.15*(bin+.5);
    rays.push_back({{0,0,.073},{2.1,.10,.073+2*(z-.073)}});
  }
  return rays;
}
int value(EvidenceGrid& g,double t,int cell=830) {
  std::vector<int8_t> a,b; g.snapshot(t,a,b); return a[cell];
}
int main() {
  { auto g=grid();
    for(int i=0;i<4;++i) g.observe(clearRays(),1+i*.21,0,0,0);
    assert(value(g,1.7)==0); // full-height repeated free evidence clears prior
    assert(value(g,1.7,1230)==100); // unseen wall untouched
    assert(value(g,7)==100); // expiry restores prior, not free
    std::vector<int8_t> a,b; g.snapshot(1.7,a,b); assert(b[830]==0);
    auto costs=inflate(a,40,40,.1); assert(costs[830]==0); // old inflation removed
  }
  { auto g=grid();
    for(int i=0;i<20;++i) g.observe(clearRays(4),1+i*.2,0,0,0);
    assert(value(g,5)==100); // high beam cannot clear low box
    g.observe({},5.2,0,0,0); assert(value(g,100)==100);
  }
  { auto g=grid();
    for(int i=0;i<20;++i) g.observe({{{0,0,.073},{.8,.04,0}}},1+i*.2,0,0,0);
    assert(value(g,5)==100); // nearer obstacle occludes old one
  }
  { auto g=grid(0); auto rays=std::vector<Ray>{{{0,0,.073},{1.05,.05,0}}};
    g.observe(rays,1,0,0,0); assert(value(g,1)==0);
    g.observe(rays,1.2,0,0,0); assert(value(g,1.2)==100);
    assert(value(g,100)==100); // new obstacle NEVER disappears by timeout
    std::vector<int8_t> a,b; g.snapshot(1.2,a,b); assert(b[830]==0);
    auto costs=inflate(a,40,40,.1); assert(costs[830]==254 && costs[831]==253);
    assert(costs[837]>0 && costs[838]==0); // ceil(.65/.1)=7-cell ROS inflation radius
    for(int i=0;i<4;++i) g.observe(clearRays(),2+i*.21,0,0,0);
    assert(value(g,2.7)==0); // observed removal clears a NEW obstacle too
  }
  { auto g=grid();
    for(int i=0;i<10;++i) g.observe(clearRays(),1,0,0,0);
    assert(value(g,1)==100); // duplicates not distinct observations
    g.observe(clearRays(),1.2,0,0,0); g.observe({},1.3,0,0,0);
    g.observe(clearRays(),1.4,0,0,0); g.observe(clearRays(),1.6,0,0,0);
    assert(value(g,1.6)==100); // missing frame breaks confirmation
  }
  { auto g=grid(); auto rays=clearRays(); rays.push_back({{0,0,.073},{1.05,.05,0}});
    for(int i=0;i<8;++i) g.observe(rays,1+i*.2,0,0,0);
    assert(value(g,3)==100); // hit wins over free evidence in same scan
  }
  { auto g=grid(-1);
    g.observe({},1,0,0,0); assert(value(g,1)==-1);
    auto a=inflate(g.prior,40,40,.1); assert(a[830]==255);
  }
  { auto g=grid();
    g.observe({{{0,0,.073},{1.05,.05,-.4}}},1,0,0,0);
    assert(value(g,1)==100); // ground endpoint does not assert empty column
  }
  { auto g=grid(0);
    for(int i=0;i<4;++i) g.observe({{{0,0,.073},{1.05,.05,-.15},false}},1+i*.2,0,0,0);
    assert(value(g,2)==0); // filtered ground is not marked even inside body-relative band
  }
  std::cout << "PASS: runtime evidence, height coverage, occlusion, expiry, marking, inflation and unknowns\n";
}
