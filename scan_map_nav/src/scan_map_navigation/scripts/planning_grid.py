"""Immutable planning snapshot; topology and costs always share one revision."""
import math
from rolling_route import distance, project


class PlanningGrid:
    def __init__(self, msg):
        self.info, self.revision, self.stamp = msg.info, msg.revision, msg.header.stamp
        self.width, self.height, self.resolution = msg.info.width, msg.info.height, msg.info.resolution
        self.occupancy, self.topology, self.costs = msg.occupancy, msg.topology, msg.costs
        origin=msg.info.origin
        if (not msg.valid or msg.header.frame_id != 'map' or self.width<=0 or self.height<=0 or
                not math.isfinite(self.resolution) or self.resolution <= 0 or
                not all(math.isfinite(v) for v in (origin.position.x,origin.position.y,
                    origin.orientation.x,origin.orientation.y,origin.orientation.z,origin.orientation.w)) or
                abs(origin.orientation.x)+abs(origin.orientation.y)+abs(origin.orientation.z)>1e-6 or
                abs(origin.orientation.w-1)>1e-6 or
                len(self.occupancy) != self.width*self.height or
                len(self.topology) != len(self.occupancy) or len(self.costs) != len(self.occupancy)):
            raise ValueError('Invalid planning-grid snapshot')
        self.ox,self.oy = msg.info.origin.position.x,msg.info.origin.position.y

    def cell(self, x, y):
        ix,iy = math.floor((x-self.ox)/self.resolution),math.floor((y-self.oy)/self.resolution)
        return iy*self.width+ix if 0 <= ix < self.width and 0 <= iy < self.height else None

    def visible(self, a, b, topology=True):
        cells = self.topology if topology else self.occupancy
        n = max(1,math.ceil(distance(a,b)/(self.resolution*.5)))
        for i in range(n+1):
            u=i/n
            idx=self.cell(a[0]+u*(b[0]-a[0]),a[1]+u*(b[1]-a[1]))
            if idx is None or cells[idx]<0 or cells[idx]>=65:
                return False
        return True

    def footprint(self, point, yaw, topology=False):
        cells=self.topology if topology else self.occupancy
        r=.35+self.resolution*math.sqrt(.5)
        for sign in (-1,1):
            x=point[0]+sign*.18*math.cos(yaw)
            y=point[1]+sign*.18*math.sin(yaw)
            lo=self.cell(x-r,y-r); hi=self.cell(x+r,y+r)
            if lo is None or hi is None:
                return False
            for iy in range(lo//self.width,hi//self.width+1):
                for ix in range(lo%self.width,hi%self.width+1):
                    wx=self.ox+(ix+.5)*self.resolution
                    wy=self.oy+(iy+.5)*self.resolution
                    if math.hypot(wx-x,wy-y)<=r and not 0 <= cells[iy*self.width+ix] < 65:
                        return False
        return True

    def route_blocked(self, route, horizon=2.0):
        # Full body corridor, independent of the 0.9m target lookahead.
        start,end=route.progress,min(route.lengths[-1],route.progress+horizon)
        n=max(1,math.ceil((end-start)/.1))
        for i in range(n+1):
            arc=start+(end-start)*i/n
            p=route.at(arc)
            a,b=route.at(max(start,arc-.05)),route.at(min(end,arc+.05))
            yaw=math.atan2(b[1]-a[1],b[0]-a[0])
            if not self.footprint(p,yaw):
                return True
        return False

    def candidate(self, route, robot, lookahead, corner_cut=.12):
        # Search the distal band, not every intervening point: a new box may be
        # BETWEEN robot and target. Unremoved prior walls may not be shortcut.
        start=route.progress
        end=min(route.lengths[-1],start+lookahead)
        arcs=[end]
        lower=max(start+.25,end-.2) if lookahead>.9+1e-6 else start+.05
        arcs.extend(s for s in route.lengths if lower < s < end)
        for arc in sorted(set(arcs),reverse=True):
            p=route.at(arc)
            probes=[v for s,v in zip(route.lengths,route.points) if start < s < arc]
            if any(project(v,route.at(start),p)[2]>corner_cut for v in probes):
                continue
            if not self.visible(robot,p,True):
                continue
            # Entire straight connection must respect prior topology, even if
            # recent additions along it may be locally detoured by SCAN.
            yaw=math.atan2(p[1]-robot[1],p[0]-robot[0])
            n=max(1,math.ceil(distance(robot,p)/.1))
            if any(not self.footprint((robot[0]+i/n*(p[0]-robot[0]),robot[1]+i/n*(p[1]-robot[1])),yaw,True)
                   for i in range(1,n+1)):
                continue
            idx=self.cell(*p)
            if idx is not None and self.costs[idx]<253 and self.footprint(p,yaw):
                return (p,arc>=route.lengths[-1]-1e-6)
        return None


class BlockageConfirmation:
    def __init__(self, duration=1.0):
        self.duration=duration
        self.since=None
        self.revisions=set()

    def update(self, blocked, revision, now):
        if not blocked:
            self.since=None; self.revisions.clear()
            return False
        if self.since is None:
            self.since=now
        self.revisions.add(revision)
        return now-self.since>=self.duration and len(self.revisions)>=2


class AdaptiveLookahead:
    """Bounded temporary trial ladder. No ROS calls and no velocity authority."""
    def __init__(self, distances=(.9,1.3,1.6,2.), stage_budget=10., total_budget=30., restore_time=1.5):
        self.distances=distances
        self.stage_budget,self.total_budget,self.restore_time=stage_budget,total_budget,restore_time
        self.stage=0
        self.started=self.stage_started=0.
        self.clear_since=None
        self.target=None

    @property
    def distance(self):
        return self.distances[self.stage]

    def advance(self, now, choose):
        if self.exhausted(now):
            return None
        if not self.stage:
            self.started=now
        while self.stage+1<len(self.distances):
            self.stage+=1
            choice=choose(self.distance)
            if choice is not None and (self.target is None or distance(choice[0],self.target[0])>.10):
                self.target=choice; self.stage_started=now; self.clear_since=None
                return choice
        return None

    def expired(self, now):
        return self.stage and (now-self.stage_started>=self.stage_budget or now-self.started>=self.total_budget)

    def exhausted(self, now):
        return self.stage and now-self.started>=self.total_budget

    def restore(self, clear_and_tracking, now):
        if not self.stage or not clear_and_tracking:
            self.clear_since=None
            return False
        if self.clear_since is None:
            self.clear_since=now
        if now-self.clear_since<self.restore_time:
            return False
        self.stage-=1
        self.stage_started=now; self.clear_since=now; self.target=None
        return True
