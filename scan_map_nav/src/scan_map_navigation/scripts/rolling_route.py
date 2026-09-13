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
        self.lookahead, self.corner_cut = lookahead, corner_cut

    def at(self, arc):
        arc = max(0,min(self.lengths[-1],arc))
        for i in range(len(self.points)-1):
            if arc <= self.lengths[i+1]:
                u = (arc-self.lengths[i])/(self.lengths[i+1]-self.lengths[i])
                a,b = self.points[i:i+2]
                return a[0]+u*(b[0]-a[0]), a[1]+u*(b[1]-a[1])
        return self.points[-1]

    def select(self, robot, visible=lambda a,b: True):
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
        end = min(self.lengths[-1],self.progress+self.lookahead)
        # Limit chord cutting against the actual polyline, including all bends.
        candidates = [s for s in self.lengths if self.progress+0.05 < s <= end]
        candidates.append(end)
        chosen = None
        for arc in sorted(set(candidates)):
            target = self.at(arc)
            probes = [self.at(self.progress)] + [p for s,p in zip(self.lengths,self.points)
                                               if self.progress < s < arc]
            if any(project(p,self.at(self.progress),target)[2] > self.corner_cut for p in probes):
                break
            if not visible(robot,target):
                break
            chosen = (target,arc >= self.lengths[-1]-1e-6)
        return chosen, best[0]
