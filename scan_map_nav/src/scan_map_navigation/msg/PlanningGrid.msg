# Coherent snapshot. Source /runtime_grid has no costs; global planner adds them.
# header.stamp is the accepted sensor observation, NOT the publication time.
std_msgs/Header header
uint64 revision
bool valid
nav_msgs/MapMetaData info
int8[] occupancy
# Static prior with ONLY confirmed removals. Added obstacles are not walls.
int8[] topology
# Native costmap values: 0 free, 253 inscribed, 254 occupied, 255 unknown.
uint8[] costs
