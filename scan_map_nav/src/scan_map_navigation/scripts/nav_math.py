"""ROS-independent geometry shared by navigation and tests."""
import math


def angle(a):
    return math.atan2(math.sin(a), math.cos(a))


def integrate(x, y, yaw, vx, vy, wz, dt):
    if abs(wz) < 1e-8:
        return (x + (math.cos(yaw)*vx-math.sin(yaw)*vy)*dt,
                y + (math.sin(yaw)*vx+math.cos(yaw)*vy)*dt, yaw)
    end = yaw + wz*dt
    return (x + (vx*(math.sin(end)-math.sin(yaw)) + vy*(math.cos(end)-math.cos(yaw)))/wz,
            y + (vx*(math.cos(yaw)-math.cos(end)) + vy*(math.sin(end)-math.sin(yaw)))/wz,
            angle(end))


def thin_points(points, spacing=0.25):
    """Keep endpoints and significant corners, suppress nearly duplicate samples."""
    if not points:
        return []
    out = [points[0]]
    for i, p in enumerate(points[1:-1], 1):
        a, b = points[i-1], points[i+1]
        corner = abs(angle(math.atan2(b[1]-p[1], b[0]-p[0]) -
                           math.atan2(p[1]-a[1], p[0]-a[0]))) > 0.15
        dist = math.hypot(p[0]-out[-1][0], p[1]-out[-1][1])
        if dist >= spacing or (corner and dist > 0.05):
            out.append(p)
    if math.hypot(points[-1][0]-out[-1][0], points[-1][1]-out[-1][1]) > 0.03:
        out.append(points[-1])
    else:
        out[-1] = points[-1]
    return out


def fresh(received, stamp, wall_now, ros_now, timeout):
    return (received is not None and 0 <= wall_now-received <= timeout and
            stamp > 0 and -0.2 <= ros_now-stamp <= timeout)
