"""Stable ordered map-frame guides; SCAN owns the path between guides.

Static visibility only preserves corridor topology. It is not a footprint or
dynamic-obstacle proof, nor a per-command motion filter.
"""
import math
from rolling_route import distance, project


def local_jump_probes(robot, target, radius=1.0):
    """Measure TF discontinuity locally, not amplified by a distant guide."""
    target = target if target is not None else robot
    d = distance(robot,target)
    u = min(1.0,radius/d) if d > 1e-9 else 0.0
    return [robot,(robot[0]+u*(target[0]-robot[0]),robot[1]+u*(target[1]-robot[1]))]


class SparseRoute:
    def __init__(self, points, visible=lambda a,b: True, spacing=3.0,
                 corner_tolerance=0.15, reach_radius=0.45):
        if not all(math.isfinite(v) and v > 0 for v in (spacing,corner_tolerance,reach_radius)):
            raise ValueError('Invalid sparse guide parameters')
        source = []
        for point in points:
            p = tuple(point[:2])
            if len(p) != 2 or not all(math.isfinite(v) for v in p):
                raise ValueError('Non-finite route point')
            if not source or distance(p,source[-1]) > 1e-6:
                source.append(p)
        if len(source) < 2:
            raise ValueError('Route has fewer than two distinct points')

        # RDP with a map visibility condition: an apparently small geometric
        # bend cannot be removed if its replacement chord crosses a wall.
        keep = {0,len(source)-1}
        pending = [(0,len(source)-1)]
        while pending:
            lo,hi = pending.pop()
            a,b = source[lo],source[hi]
            clear = visible(a,b)
            if hi == lo+1:
                if not clear:
                    raise ValueError('Global route segment crosses occupied/unknown map')
                continue
            error,index = max((project(source[i],a,b)[2],i) for i in range(lo+1,hi))
            if clear and error <= corner_tolerance:
                continue
            split = index if error > 1e-9 else (lo+hi)//2
            keep.add(split)
            pending.extend(((lo,split),(split,hi)))
        anchors = [source[i] for i in sorted(keep)]
        self.points = [anchors[0]]
        for a,b in zip(anchors,anchors[1:]):
            count = max(1,int(math.ceil(distance(a,b)/spacing)))
            for i in range(1,count+1):
                u = i/count
                self.points.append((a[0]+u*(b[0]-a[0]),a[1]+u*(b[1]-a[1])))
        self.index = 1
        self.reach_radius = reach_radius

    def select(self, robot, visible=lambda a,b: True):
        # Never select the globally nearest guide: that would skip branches at
        # a crossing or jump through a wall into a parallel return corridor.
        while self.index < len(self.points)-1:
            a,b = self.points[self.index-1:self.index+1]
            dx,dy = b[0]-a[0],b[1]-a[1]
            length = distance(a,b)
            passed = ((robot[0]-b[0])*dx+(robot[1]-b[1])*dy >= 0 and
                      abs((robot[0]-b[0])*dy-(robot[1]-b[1])*dx)/length <= self.reach_radius)
            if not (distance(robot,b) <= self.reach_radius or passed):
                break
            if not visible(robot,self.points[self.index+1]):
                # SCAN rejects goals <0.2m away. If a corner cannot be passed
                # without crossing a wall, ask for a fresh global route rather
                # than repeatedly submit that almost-reached intermediate goal.
                if distance(robot,b) < 0.22:
                    return None,project(robot,a,b)[2]
                break
            self.index += 1
        a,b = self.points[self.index-1:self.index+1]
        return (b,self.index == len(self.points)-1),project(robot,a,b)[2]


class GuideProgress:
    """Allow temporary detours; bound prolonged loss of useful guide progress."""
    def __init__(self, timeout=45.0, max_deviation=3.0, deviation_timeout=3.0):
        self.timeout,self.max_deviation,self.deviation_timeout = timeout,max_deviation,deviation_timeout
        self.index = None
        self.best = float('inf')
        self.progress_at = 0.0
        self.deviated_at = None

    def update(self, index, remaining, deviation, now):
        if self.index != index:
            self.index,self.best,self.progress_at = index,remaining,now
            self.deviated_at = None
        elif remaining < self.best-0.1:
            self.best,self.progress_at = remaining,now
        if deviation > self.max_deviation:
            if self.deviated_at is None:
                self.deviated_at = now
            elif now-self.deviated_at >= self.deviation_timeout:
                return 'Persistent excessive deviation from active guide segment'
        else:
            self.deviated_at = None
        if now-self.progress_at >= self.timeout:
            return 'No useful progress toward active guide'
        return ''
