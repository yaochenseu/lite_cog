# Short-lived task lease, not a velocity command. No manual arm step.
std_msgs/Header header
uint32 epoch
uint64 task_id
uint8 STOP=0
uint8 TRACK=1
uint8 ALIGN=2
uint8 mode
float64 yaw
