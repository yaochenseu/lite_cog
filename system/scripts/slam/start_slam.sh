#!/bin/sh

#开启建图程序
gnome-terminal -x bash -c "source /home/ysc/lite_cog/slam/devel/setup.bash; roslaunch faster_lio mapping_c16.launch; read -p 'Press any key to exit...'"

#开启生成grid_map终端
gnome-terminal -x bash -c "bash /home/ysc/lite_cog/system/scripts/slam/gridmap.sh; read -p 'Press any key to exit...'"

# 开启保存地图终端
gnome-terminal -x bash -c "bash /home/ysc/lite_cog/system/scripts/slam/save_map.sh; read -p 'Press any key to exit...'"

