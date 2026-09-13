#!/bin/bash

#注意，项目名称一定是中划线“-”
PROJECT_NAME=system-monitor

rm -fR debian obj-x86_64-linux-gnu ../*${PROJECT_NAME}*.deb

bloom-generate rosdebian --os-name ubuntu --ros-distro noetic
sed -i "s/dh_shlibdeps -l/dh_shlibdeps --dpkg-shlibdeps-params=--ignore-missing-info -l/g" debian/rules
fakeroot debian/rules binary

#read -n 1 -s -r -p "Press any key to continue"

rm -fR debian obj-x86_64-linux-gnu
