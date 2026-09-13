#!/bin/bash

#输入save时才保存地图
echo "INPUT: 1 (when you want to creat the grid map)"
read COMMAND
case "$COMMAND" in
    "1")
        echo "YYYYYY"
	source /home/ysc/lite_cog/slam/devel/setup.bash;
	roslaunch pcd2grid pcd2grid.launch
        ;;
    *)
        echo "wrong"
        ;;
esac
