std_msgs/Header header
uint32 epoch
uint64 task_id
geometry_msgs/Point position
bool final_goal
# Explicit recovery replacement. Zero means ordinary rolling update.
uint64 recovery_id
uint64 expected_generation
