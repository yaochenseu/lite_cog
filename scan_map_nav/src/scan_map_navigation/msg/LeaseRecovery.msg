# Gate requests a reset handshake after a transient control lease timeout.
# Navigator echoes the identity only AFTER resetting planner and controller.
std_msgs/Header header
uint64 recovery_id
uint64 task_id
uint32 epoch
uint64 generation
