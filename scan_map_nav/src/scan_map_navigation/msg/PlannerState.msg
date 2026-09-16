# Liveness is separate (/scan_local/heartbeat). This describes execution safety.
std_msgs/Header header
uint32 epoch
uint64 task_id
# Incremented when a trajectory is revoked; queued old velocities cannot resume.
uint64 generation
uint64 target_revision
uint32 recovery_attempts
uint8 IDLE=0
uint8 PLANNING=1
uint8 TRACKING=2
uint8 RECOVERING=3
uint8 BLOCKED=4
uint8 ALIGNING=5
uint8 state
string reason
