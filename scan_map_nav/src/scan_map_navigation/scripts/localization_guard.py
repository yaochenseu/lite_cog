"""Multi-frame localization correction validation, without ROS or motion output."""
import math
from rolling_route import correction_size, distance


class LocalizationJumpGuard:
    def __init__(self, distance_limit=.8, yaw_limit=.5, confirm_frames=5,
                 confirm_time=.3, recover_frames=3, recover_time=.15, hold_timeout=2.):
        if any(type(n) is not int or n < 2 for n in (confirm_frames,recover_frames)):
            raise ValueError('Jump confirmation/recovery needs at least two frames')
        if any(not math.isfinite(v) or v <= 0 for v in
               (distance_limit,yaw_limit,confirm_time,recover_time,hold_timeout)):
            raise ValueError('Invalid localization jump threshold/time')
        if hold_timeout <= max(confirm_time,recover_time):
            raise ValueError('Jump hold timeout must exceed confirmation/recovery time')
        self.distance_limit,self.yaw_limit = distance_limit,yaw_limit
        self.confirm_frames,self.confirm_time = confirm_frames,confirm_time
        self.recover_frames,self.recover_time = recover_frames,recover_time
        self.hold_timeout = hold_timeout
        self.reset()

    def reset(self):
        self.anchor = None
        self.probes = []
        self.last_stamp = -1
        self.pending = False
        self.started = self.bad_started = self.good_started = None
        self.bad_count = self.good_count = 0
        self.shift = self.turn = 0.

    def accept(self,transform,robot,target):
        self.anchor = tuple(transform)
        xy = tuple(robot[:2])
        self.probes = [xy]
        if target is not None:
            d = distance(xy,target)
            scale = 1./d if d > 1. else 1.
            self.probes.append((xy[0]+(target[0]-xy[0])*scale,
                                xy[1]+(target[1]-xy[1])*scale))
        self.pending = False
        self.started = self.bad_started = self.good_started = None
        self.bad_count = self.good_count = 0

    def observe(self,stamp,transform,robot,target,now):
        fresh = stamp > self.last_stamp
        if fresh:
            self.last_stamp = stamp
        if self.anchor is None:
            self.accept(transform,robot,target)
            return 'OK'
        # Freeze both reference transform AND local probes throughout a hold.
        # A permanent one-time step must not become the next "normal" baseline.
        self.shift,self.turn = correction_size(self.anchor,transform,self.probes)
        bad = self.shift > self.distance_limit or self.turn > self.yaw_limit
        if not self.pending and not bad:
            if fresh:
                self.accept(transform,robot,target)
            return 'OK'
        if not self.pending:
            self.pending,self.started = True,now
        if fresh:
            if bad:
                if not self.bad_count:
                    self.bad_started = now
                self.bad_count += 1
                self.good_count,self.good_started = 0,None
                if self.bad_count >= self.confirm_frames and now-self.bad_started >= self.confirm_time:
                    raise RuntimeError('Persistent localization jump: %d fresh frames, %.3f m / %.1f deg; check RViz and resend goal' %
                                       (self.bad_count,self.shift,math.degrees(self.turn)))
            else:
                if not self.good_count:
                    self.good_started = now
                self.good_count += 1
                self.bad_count,self.bad_started = 0,None
                if self.good_count >= self.recover_frames and now-self.good_started >= self.recover_time:
                    self.accept(transform,robot,target)
                    return 'RECOVERED'
        if now-self.started >= self.hold_timeout:
            raise RuntimeError('Localization jump did not settle within %.1f s (bad=%d, good=%d); check RViz' %
                               (self.hold_timeout,self.bad_count,self.good_count))
        return 'HOLD'
