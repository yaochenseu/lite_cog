#!/bin/bash

#输入save时才保存地图
echo "INPUT: 2 (when you want to save the grid map)"
read COMMAND
case "$COMMAND" in
    "2")
        echo "YYYYYY"
	source /home/ysc/lite_cog/slam/devel/setup.bash;
	rosrun map_server map_saver -f /home/ysc/lite_cog/system/map/lite3
        ;;
    *)
        echo "wrong"
        ;;
esac
