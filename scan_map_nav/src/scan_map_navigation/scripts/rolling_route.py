"""Ordered map-frame route following. No ROS calls or velocity decisions."""
import math
from nav_math import angle


def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])


def project(p, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    length2 = dx*dx+dy*dy
    u = 0 if length2 < 1e-12 else max(0, min(1, ((p[0]-a[0])*dx+(p[1]-a[1])*dy)/length2))
    q = (a[0]+u*dx, a[1]+u*dy)
    return u, q, distance(p, q)


def planar_transform(map_pose, odom_pose):
    """Same-stamp body poses define an SE(2) map->odom conversion.

    Avoid projecting a tilted NDT map plane using an unrelated body height.
    """
    yaw = angle(odom_pose[2]-map_pose[2])
    c, s = math.cos(yaw), math.sin(yaw)
    return (odom_pose[0]-c*map_pose[0]+s*map_pose[1],
            odom_pose[1]-s*map_pose[0]-c*map_pose[1], yaw)


def transform_point(transform, point):
    x, y, yaw = transform
    c, s = math.cos(yaw), math.sin(yaw)
    return x+c*point[0]-s*point[1], y+s*point[0]+c*point[1]


def correction_size(old, new, probes):
    return max(distance(transform_point(old,p), transform_point(new,p)) for p in probes), abs(angle(new[2]-old[2]))


class OrderedRoute:
    def __init__(self, points, lookahead=0.9, corner_cut=0.12):
        self.points = []
        for p in points:
            p = tuple(p[:2])
            if not self.points or distance(p,self.points[-1]) > 0.01:
                self.points.append(p)
        if len(self.points) < 2:
            raise ValueError('Route has fewer than two distinct points')
        self.lengths = [0.0]
        for a,b in zip(self.points,self.points[1:]):
            self.lengths.append(self.lengths[-1]+distance(a,b))
        self.progress = 0.0
        self.selected_arc = None
        self.lookahead, self.corner_cut = lookahead, corner_cut

    def at(self, arc):
        arc = max(0,min(self.lengths[-1],arc))
        for i in range(len(self.points)-1):
            if arc <= self.lengths[i+1]:
                u = (arc-self.lengths[i])/(self.lengths[i+1]-self.lengths[i])
                a,b = self.points[i:i+2]
                return a[0]+u*(b[0]-a[0]), a[1]+u*(b[1]-a[1])
        return self.points[-1]

    def advance(self, robot):
        # Search only locally along path order: no nearest-point jumps to a
        # remote branch at a crossing or a nearby return corridor.
        limit = min(self.lengths[-1],self.progress+0.5)
        best = (distance(robot,self.at(self.progress)),self.progress)
        for i,(a,b) in enumerate(zip(self.points,self.points[1:])):
            lo,hi = max(self.progress,self.lengths[i]),min(limit,self.lengths[i+1])
            if hi < lo:
                continue
            u,_,d = project(robot,self.at(lo),self.at(hi))
            if d < best[0]-1e-6:
                best = d,lo+u*(hi-lo)
        self.progress = best[1]
        return best[0]

    def select(self, robot, visible=lambda a,b: True):
        deviation = self.advance(robot)
        end = min(self.lengths[-1],self.progress+self.lookahead)
        # Limit chord cutting against the actual polyline, including all bends.
        candidates = [s for s in self.lengths if self.progress+0.05 < s <= end]
        candidates.append(end)
        chosen = None
        self.selected_arc = None
        for arc in sorted(set(candidates)):
            target = self.at(arc)
            probes = [self.at(self.progress)] + [p for s,p in zip(self.lengths,self.points)
                                               if self.progress < s < arc]
            if any(project(p,self.at(self.progress),target)[2] > self.corner_cut for p in probes):
                break
            if not visible(robot,target):
                break
            chosen = (target,arc >= self.lengths[-1]-1e-6)
            self.selected_arc = arc
        return chosen, deviation

    def checked_target(self, robot, arc, visible=lambda a,b: True):
        """Exact forward arc target, not a nearest-point jump to another branch."""
        arc = min(self.lengths[-1],arc)
        if arc < self.progress-1e-6:
            return None
        target = self.at(arc)
        probes = [self.at(self.progress)] + [p for s,p in zip(self.lengths,self.points)
                                           if self.progress < s < arc]
        if any(project(p,self.at(self.progress),target)[2] > self.corner_cut for p in probes):
            return None
        if not visible(robot,target):
            return None
        return target,arc >= self.lengths[-1]-1e-6


class GuideRecovery:
    """After failed rounds, extend by one step up to a bounded path horizon."""
    def __init__(self, failures=3, step=.5, max_ahead=5., motion=.2):
        if type(failures) is not int or failures < 1:
            raise ValueError('Invalid guide_extension_failures')
        if any(not math.isfinite(x) or x <= 0 for x in (step,max_ahead,motion)):
            raise ValueError('Invalid guide extension step/horizon/motion')
        self.threshold,self.step,self.max_ahead,self.motion = failures,step,max_ahead,motion
        self.reset()

    def reset(self):
        self.active_arc = self.last_odom = None
        self.reset_trials()

    def reset_trials(self):
        self.failures = 0
        self.base_arc = self.pending_arc = self.limit_arc = self.motion_anchor = None
        self.reason = 'Waiting for failed local rounds'

    def observe_motion(self, odom_xy, tracking):
        # Continuous leg odometry, not a map/NDT correction or a TRACKING label.
        self.last_odom = tuple(odom_xy[:2])
        if (tracking and self.motion_anchor is not None and
                distance(self.last_odom,self.motion_anchor) >= self.motion):
            self.reset_trials()  # Keep the working guide until normal selection catches up.
            return True
        return False

    def relaxed_target(self,route,robot,arc,allowed):
        # A recovery guide is an intention, not a straight-line motion command.
        # Keep path order and endpoint bounds; SCAN checks the REAL trajectory.
        if arc < route.progress-1e-6 or arc > route.lengths[-1]+1e-6:
            return None
        point = route.at(arc)
        if not allowed(robot,point):
            return None
        return point,arc >= route.lengths[-1]-1e-6

    def choose(self, route, robot, normal, allowed):
        if self.active_arc is not None:
            if normal is not None and route.selected_arc >= self.active_arc-1e-6:
                self.active_arc = None  # Catch-up alone is not proof of body movement.
            else:
                candidate = self.relaxed_target(route,robot,self.active_arc,allowed)
                if candidate is not None:
                    return candidate,self.active_arc
                self.active_arc = None  # Unknown/out-of-map is still not permitted.
        return normal,route.selected_arc

    def failed(self, route, robot, sent_arc, allowed):
        self.failures += 1
        self.motion_anchor = self.last_odom
        self.pending_arc = None
        if self.failures < self.threshold:
            self.reason = 'Same guide until %d failed rounds (%d so far)' % (self.threshold,self.failures)
            return None
        if self.base_arc is None:
            self.base_arc = sent_arc
            # Freeze this episode's ceiling: map jitter cannot keep moving it away.
            self.limit_arc = min(route.lengths[-1],route.progress+self.max_ahead)
        lower = max(sent_arc,self.active_arc if self.active_arc is not None else sent_arc)
        endpoint = route.lengths[-1]
        # If the existing guide already IS the endpoint, explicitly try it once
        # in relaxed mode after the third failure. Never extrapolate beyond it.
        endpoint_trial = lower >= endpoint-1e-6 and self.active_arc is None
        if lower >= self.limit_arc-1e-6 and not endpoint_trial:
            self.reason = 'Endpoint already active; retrying endpoint' if lower >= endpoint-1e-6 else 'Maximum guide distance reached; retrying current guide'
            return None
        arc = endpoint if endpoint_trial else min(self.limit_arc,lower+self.step)
        candidate = self.relaxed_target(route,robot,arc,allowed)
        if candidate is None:
            self.reason = 'Recovery guide rejected: unknown/out-of-map or invalid path order; no advance consumed'
            return None
        self.pending_arc = arc
        self.reason = ('Trying endpoint' if candidate[1] else 'Trying next %.2f m path step' % self.step) + '; static occupied cells/corner shortcut allowed, SCAN collision checks required'
        return candidate,arc,max(0.,arc-self.base_arc)

    def commit(self,arc):
        # Only a target actually published by the manager consumes advancement.
        if self.pending_arc is None or abs(arc-self.pending_arc) > 1e-6:
            raise ValueError('No matching recovery guide proposal to commit')
        self.active_arc = arc
        self.pending_arc = None
