"""Local, origin-independent route displacement and bounded stability checks."""
import math
import numpy as np
from nav_math import angle


def nearby_probes(reference, odom_position, points, horizon=1.5):
    """Map-frame robot anchor plus the next local section of the saved map path."""
    anchor = np.linalg.solve(reference, np.array([*odom_position, 1.0]))
    probes = [anchor[:3]]
    route = [np.array([p[0], p[1], 0.0]) for p in points]
    if len(route) < 2:
        return probes + route
    best = None
    for i, (a, b) in enumerate(zip(route, route[1:])):
        d = b[:2]-a[:2]
        u = np.clip(np.dot(anchor[:2]-a[:2], d)/max(np.dot(d,d), 1e-12), 0, 1)
        projection = a+u*(b-a)
        distance = np.linalg.norm(projection[:2]-anchor[:2])
        if best is None or distance < best[0]:
            best = (distance, i, projection)
    _, index, previous = best
    probes.append(previous)
    remaining = horizon
    for endpoint in route[index+1:]:
        distance = np.linalg.norm(endpoint[:2]-previous[:2])
        if distance > remaining:
            probes.append(previous+(endpoint-previous)*(remaining/distance))
            break
        probes.append(endpoint)
        remaining -= distance
        previous = endpoint
        if remaining <= 0:
            break
    return probes


def transform_shift(before, after, probes):
    if not np.isfinite(before).all() or not np.isfinite(after).all():
        raise ValueError('Non-finite localization transform')
    distance = 0.0
    for point in probes:
        p = np.array([*point, 1.0])
        distance = max(distance, float(np.linalg.norm(((after-before).dot(p))[:2])))
    yaw = abs(angle(math.atan2(after[1,0],after[0,0])-math.atan2(before[1,0],before[0,0])))
    return distance, yaw


class StableTransformWindow:
    def __init__(self, duration, distance_tolerance, yaw_tolerance):
        self.duration = duration
        self.distance_tolerance = distance_tolerance
        self.yaw_tolerance = yaw_tolerance
        self.since = None
        self.reference = None

    def update(self, now, transform, probes, stopped=True):
        if not stopped or transform is None:
            self.since = self.reference = None
            return False
        if self.reference is not None:
            distance, yaw = transform_shift(self.reference, transform, probes)
            if distance > self.distance_tolerance or yaw > self.yaw_tolerance:
                self.since = self.reference = None
        if self.reference is None:
            self.reference = transform.copy()
            self.since = now
        return now-self.since >= self.duration


class RefreshBudget:
    def __init__(self, maximum, cooldown):
        self.maximum = maximum
        self.cooldown = cooldown
        self.count = 0
        self.last_plan = -float('inf')

    def begin(self):
        if self.count >= self.maximum:
            raise RuntimeError('Localization route refresh limit reached; check localization before retrying')
        self.count += 1

    def cooled_down(self, now):
        return now-self.last_plan >= self.cooldown
