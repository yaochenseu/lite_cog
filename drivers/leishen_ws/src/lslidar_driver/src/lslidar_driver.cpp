/******************************************************************************
 * This file is part of lslidar_cx driver.
 *
 * Copyright 2022 LeiShen Intelligent Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *****************************************************************************/

#include "lslidar_driver/lslidar_driver.h"
#include <std_msgs/String.h>
#include <thread>
#include <sensor_msgs/point_cloud2_iterator.h>

#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/filters/conditional_removal.h>
#include <pcl/filters/crop_box.h>
#include <pcl/filters/filter.h>
#include <pcl/filters/radius_outlier_removal.h>
#include <pcl/filters/statistical_outlier_removal.h>

namespace lslidar_driver {
    lslidarDriver::lslidarDriver(ros::NodeHandle &node, ros::NodeHandle &private_nh) : nh(node),
                                                                                       pnh(private_nh),
                                                                                       last_azimuth(0),
                                                                                       sweep_end_time(0.0),
                                                                                       is_first_sweep(true),
                                                                                       return_mode(1),
                                                                                       packet_rate(1695.0),
                                                                                       current_packet_time(0.0),
                                                                                       last_packet_time(0.0),
                                                                                       current_point_time(0.0),
                                                                                       last_point_time(0.0),
                                                                                       horizontal_angle_resolution(0.0),
                                                                                       lidar_nuber_(1),
                                                                                       sweep_data(
                                                                                               new lslidar_msgs::LslidarScan()),
                                                                                       sweep_data_bak(
                                                                                               new lslidar_msgs::LslidarScan()) {
        return;
    }

    bool lslidarDriver::checkPacketValidity(const lslidar_driver::RawPacket *packet) {
        for (size_t blk_idx = 0; blk_idx < BLOCKS_PER_PACKET; ++blk_idx) {
            if (packet->blocks[blk_idx].header != UPPER_BANK) {
                return false;
            }
        }
        return true;
    }

    bool lslidarDriver::isPointInRange(const double &distance) {
        return (distance >= min_range && distance < max_range);
    }

    bool lslidarDriver::loadParameters() {
        pnh.param("pcap", dump_file, std::string(""));
        pnh.param("packet_rate", packet_rate, 1695.0);
        pnh.param<std::string>("frame_id", frame_id, "laser_link");
        pnh.param<std::string>("lidar_type", lidar_type, "c16");
        pnh.param<bool>("add_multicast", add_multicast, false);
        pnh.param<std::string>("c32_type", c32_type, "c32_32");
        pnh.param<bool>("pcl_type", pcl_type, false);
        pnh.param("group_ip", group_ip_string, std::string("234.2.3.2"));
        pnh.param("device_ip", lidar_ip_string, std::string("192.168.1.200"));
        pnh.param("msop_port", msop_udp_port, (int) MSOP_DATA_PORT_NUMBER);
        pnh.param("difop_port", difop_udp_port, (int) DIFOP_DATA_PORT_NUMBER);
        pnh.param("point_num", point_num, 2000);
        pnh.param("scan_num", scan_num, 2000);
        pnh.param("min_range", min_range, 0.3);
        pnh.param("max_range", max_range, 150.0);
        pnh.param("distance_unit", distance_unit, 0.40);
        pnh.param("angle_disable_min", angle_disable_min, 0);
        pnh.param("angle_disable_max", angle_disable_max, 0);
        pnh.param("horizontal_angle_resolution", horizontal_angle_resolution, 0.2);
        pnh.param<bool>("use_gps_ts", use_gps_ts, false);
        pnh.param<bool>("publish_scan", publish_scan, false);
        pnh.param<bool>("coordinate_opt", coordinate_opt, false);
        pnh.param<std::string>("pointcloud_topic", pointcloud_topic, "lslidar_point_cloud");

        pnh.param("debug", debug_, false);

        pnh.param("filter_voxel", filter_voxel_, true);
        pnh.param("filter_leaf_size_m", filter_leaf_size_m_, 0.05);

        pnh.param("filter_box", filter_box_, true);
        pnh.param("crop_negative", crop_negative_, true);

        pnh.param("keep_organized", keep_organized_, false); 
        pnh.param("filter_front_m", filter_front_m_, 0.15);
        pnh.param("filter_back_m", filter_back_m_, 0.6);
        pnh.param("filter_left_m", filter_left_m_, 0.25);
        pnh.param("filter_right_m", filter_right_m_, 0.25);
        pnh.param("filter_lower_height_m", filter_lower_height_m_, 0.5);
        pnh.param("filter_higher_height_m", filter_higher_height_m_, 0.1);

        pnh.param("filter_plane", filter_plane_, true);
        pnh.param("plane_a", plane_a_, 0.0);
        pnh.param("plane_b", plane_b_, 0.288232);
        pnh.param("plane_c", plane_c_, 0.95756);
        pnh.param("plane_d", plane_d_, 0.0);
        pnh.param("plane_distance_threshold", plane_distance_threshold_, 0.04);
        plane_sqrt_dividend_ = sqrt(plane_a_ * plane_a_ + plane_b_ * plane_b_ + plane_c_ * plane_c_);
        pnh.param("plane_filter_x_min", plane_filter_x_min_, -0.6);
        pnh.param("plane_filter_x_max", plane_filter_x_max_, 0.6);
        pnh.param("plane_filter_y_min", plane_filter_y_min_, 0.0);
        pnh.param("plane_filter_y_max", plane_filter_y_max_, 1.7);

        ROS_INFO_STREAM("filter_vexel: " << filter_voxel_
            << " filter_leaf_size_m: " << filter_leaf_size_m_
            << " filter_box: " << filter_box_
            << " crop_negative: " << crop_negative_
            << " keep_organized: " << keep_organized_
            << " filter_front_m: " << filter_front_m_
            << " filter_back_m: " << filter_back_m_
            << " filter_left_m: " << filter_left_m_
            << " filter_right_m: " << filter_right_m_
            << " filter_lower_height_m: " << filter_lower_height_m_
            << " filter_higher_height_m: " << filter_higher_height_m_
            << " filter_plane_: " << filter_plane_
            << " plane_a: " << plane_a_
            << " plane_b: " << plane_b_
            << " plane_c: " << plane_c_
            << " plane_d: " << plane_d_
            << " plane_distance_threshold: " << plane_distance_threshold_
            << " plane_sqrt_dividend_: " << plane_sqrt_dividend_
            << " plane_filter_x_min: " << plane_filter_x_min_
            << " plane_filter_x_max: " << plane_filter_x_max_
            << " plane_filter_y_min: " << plane_filter_y_min_
            << " plane_filter_y_max: " << plane_filter_y_max_
        );

        inet_aton(lidar_ip_string.c_str(), &lidar_ip);
        if (add_multicast) ROS_INFO_STREAM("opening UDP socket: group_address " << group_ip_string);
        return true;
    }

    void lslidarDriver::initTimeStamp() {
        for (int i = 0; i < 10; i++) {
            this->packetTimeStamp[i] = 0;
        }
        this->packet_time_s = 0;
        this->packet_time_ns = 0;
        this->timeStamp = ros::Time(0.0);
    }

    bool lslidarDriver::createRosIO() {
        pointcloud_pub = nh.advertise<sensor_msgs::PointCloud2>(pointcloud_topic, 10);
        scan_pub = nh.advertise<sensor_msgs::LaserScan>("scan", 10);
        lslidar_control = nh.advertiseService("lslidarcontrol", &lslidarC16Driver::lslidarC16Control, this);

        if (dump_file != "") {
            msop_input_.reset(new lslidar_driver::InputPCAP(pnh, msop_udp_port, 1212, packet_rate, dump_file));
            difop_input_.reset(new lslidar_driver::InputPCAP(pnh, difop_udp_port, 1206, 1, dump_file));
        } else {
            msop_input_.reset(new lslidar_driver::InputSocket(pnh, msop_udp_port, 1212));
            difop_input_.reset(new lslidar_driver::InputSocket(pnh, difop_udp_port, 1206));
        }
        difop_thread_ = boost::shared_ptr<boost::thread>(
                new boost::thread(boost::bind(&lslidarDriver::difopPoll, this)));

        return true;
    }

    void lslidarDriver::difopPoll() {
        // reading and publishing scans as fast as possible.
        lslidar_msgs::LslidarPacketPtr difop_packet_ptr(new lslidar_msgs::LslidarPacket);
        while (ros::ok()) {
            // keep reading
            int rc = difop_input_->getPacket(difop_packet_ptr);
            if (rc == 0) {
                for (int i = 0; i < 1206; i++) {
                    difop_data[i] = difop_packet_ptr->data[i];
                }
/*              this->packetTimeStamp[4] = difop_packet_ptr->data[57];
                this->packetTimeStamp[5] = difop_packet_ptr->data[56];
                this->packetTimeStamp[6] = difop_packet_ptr->data[55];
                this->packetTimeStamp[7] = difop_packet_ptr->data[54];
                this->packetTimeStamp[8] = difop_packet_ptr->data[53];
                this->packetTimeStamp[9] = difop_packet_ptr->data[52];*/

            } else if (rc < 0) {
                return;
            }
            ros::spinOnce();
        }
    }

    void lslidarDriver::pointcloudToLaserscan(const sensor_msgs::PointCloud2 &cloud_msg,
                                              sensor_msgs::LaserScan &output_scan) {
        // build laserscan output_scan
        output_scan.header = cloud_msg.header;
        output_scan.header.frame_id = cloud_msg.header.frame_id;
        output_scan.angle_min = -M_PI;
        output_scan.angle_max = M_PI;
        output_scan.angle_increment = horizontal_angle_resolution * DEG_TO_RAD;
        output_scan.time_increment = 0.0;
//        output_scan.scan_time = scan_time_;
        output_scan.range_min = min_range;
        output_scan.range_max = max_range;

        // determine amount of rays to create
        uint32_t ranges_size = std::ceil((output_scan.angle_max - output_scan.angle_min) / output_scan.angle_increment);

        // determine if laserscan rays with no obstacle data will evaluate to infinity or max_range
        output_scan.ranges.assign(ranges_size, std::numeric_limits<double>::infinity());

        // Iterate through pointcloud
        for (sensor_msgs::PointCloud2ConstIterator<float> iter_x(cloud_msg, "x"), iter_y(cloud_msg, "y"),
                     iter_z(cloud_msg, "z");
             iter_x != iter_x.end(); ++iter_x, ++iter_y, ++iter_z) {
            if (std::isnan(*iter_x) || std::isnan(*iter_y) || std::isnan(*iter_z)) {
                ROS_INFO("rejected for nan in point(%f, %f, %f)\n", *iter_x, *iter_y, *iter_z);
                continue;
            }

            double range = hypot(*iter_x, *iter_y);
            if (range < min_range) {
                ROS_INFO("rejected for range %f below minimum value %f. Point: (%f, %f, %f)", range, min_range,
                         *iter_x,
                         *iter_y, *iter_z);
                continue;
            }
            if (range > max_range) {
                ROS_INFO("rejected for range %f above maximum value %f. Point: (%f, %f, %f)", range, max_range,
                         *iter_x,
                         *iter_y, *iter_z);
                continue;
            }

            double angle = atan2(*iter_y, *iter_x);
            if (angle < output_scan.angle_min || angle > output_scan.angle_max) {
                ROS_INFO("rejected for angle %f not in range (%f, %f)\n", angle, output_scan.angle_min,
                         output_scan.angle_max);
                continue;
            }

            // overwrite range at laserscan ray if new range is smaller
            int index = (angle - output_scan.angle_min) / output_scan.angle_increment;
            if (range < output_scan.ranges[index]) {
                output_scan.ranges[index] = range;
            }
        }
    }

    void lslidarDriver::publishPointcloud() {

        if (pcl_type) {
            pcl::PointCloud<pcl::PointXYZI>::Ptr point_cloud(new pcl::PointCloud<pcl::PointXYZI>);
            point_cloud->header.frame_id = frame_id;
            point_cloud->height = 1;
            point_cloud->header.stamp = static_cast<uint64_t>(sweep_end_time * 1e6);
            
            pcl::PointCloud<pcl::PointXYZI>::Ptr point_cloud_scan(new pcl::PointCloud<pcl::PointXYZI>);
            point_cloud_scan->header.frame_id = frame_id;
            point_cloud_scan->height = 1;
            point_cloud_scan->header.stamp = static_cast<uint64_t>(sweep_end_time * 1e6);            
            {            
                std::unique_lock<std::mutex> lock(pointcloud_lock);
                size_t j;
                pcl::PointXYZI point;
                pcl::PointXYZI scan_point;
                if (!sweep_data_bak->points.empty()) {
                    for (j = 0; j < sweep_data_bak->points.size(); ++j) {
                        if ((sweep_data_bak->points[j].azimuth > angle_disable_min) &&
                            (sweep_data_bak->points[j].azimuth < angle_disable_max)) {
                            continue;
                        }
                        if (scan_num == sweep_data_bak->points[j].ring) {
                            scan_point.x = sweep_data_bak->points[j].x;
                            scan_point.y = sweep_data_bak->points[j].y;
                            scan_point.z = sweep_data_bak->points[j].z;
                            scan_point.intensity = sweep_data_bak->points[j].intensity;
                            point_cloud_scan->points.push_back(scan_point);
                            ++point_cloud_scan->width;
                        }
                        point.x = sweep_data_bak->points[j].x;
                        point.y = sweep_data_bak->points[j].y;
                        point.z = sweep_data_bak->points[j].z;
                        point.intensity = sweep_data_bak->points[j].intensity;
                        point_cloud->points.push_back(point);
                        ++point_cloud->width;
                    }
                }
            }

            auto start1 = std::chrono::steady_clock::now();
            if(filter_voxel_){
                if(debug_) std::cout << "filter_voxel_ Original: " << point_cloud->size() << std::endl;
                pcl::VoxelGrid<pcl::PointXYZI> voxel_grid;
                voxel_grid.setInputCloud(point_cloud);
                voxel_grid.setLeafSize(filter_leaf_size_m_, filter_leaf_size_m_, filter_leaf_size_m_);
                voxel_grid.filter(*point_cloud);
                if(debug_) std::cout << "filter_voxel_ Filtered: " << point_cloud->size() << std::endl;  
            }            
            auto end1 = std::chrono::steady_clock::now();
            if(debug_)  std::cout << "voxel filter t_diff: " << std::chrono::duration_cast<std::chrono::microseconds>(end1-start1).count() << " us" << std::endl;

            auto start2 = std::chrono::steady_clock::now();
            if(filter_box_){
                if(debug_) std::cout << "filter_box_ Original: " << point_cloud->size() << std::endl;
                pcl::CropBox<pcl::PointXYZI> crop_box;
                crop_box.setKeepOrganized(keep_organized_);
                crop_box.setMin(Eigen::Vector4f(-filter_right_m_, -filter_front_m_, -filter_lower_height_m_, 1.0));
                crop_box.setMax(Eigen::Vector4f(filter_left_m_, filter_back_m_, filter_higher_height_m_, 1.0));
                crop_box.setNegative(crop_negative_);
                crop_box.setInputCloud(point_cloud);
                crop_box.filter(*point_cloud);
                if(debug_) std::cout << "filter_box_ Filtered: " << point_cloud->size() << std::endl;  
            }
            auto end2 = std::chrono::steady_clock::now();
            if(debug_) std::cout << "xyz filter t_diff: " << std::chrono::duration_cast<std::chrono::microseconds>(end2-start2).count() << " us" << std::endl;

            auto start3 = std::chrono::steady_clock::now();
            if(filter_plane_){
                pcl::PointCloud<pcl::PointXYZI>::Ptr cloud_filtered(new pcl::PointCloud<pcl::PointXYZI>);
                cloud_filtered->header.frame_id = frame_id;
                cloud_filtered->height = 1;
                cloud_filtered->header.stamp = static_cast<uint64_t>(sweep_end_time * 1e6);
                if(debug_) std::cout << "filter_plane_ Original: " << point_cloud->size() << std::endl;
                for(auto &point : point_cloud->points)
                {
                    if(point.x < plane_filter_x_min_
                        || point.x > plane_filter_x_max_
                        || point.y < plane_filter_y_min_
                        || point.y > plane_filter_y_max_
                        || fabs(plane_a_ * point.x + plane_b_ * point.y + plane_c_ * point.z + plane_d_) / plane_sqrt_dividend_ > plane_distance_threshold_)
                    {
                        cloud_filtered->push_back(point);
                    }
                }
                if(debug_) std::cout << "filter_plane_ Filtered: " << cloud_filtered->size() << std::endl;

                auto end3 = std::chrono::steady_clock::now();
                if(debug_)  std::cout << "plane filter t_diff: " << std::chrono::duration_cast<std::chrono::microseconds>(end3-start3).count() << " us" << std::endl << std::endl;

                sensor_msgs::PointCloud2 pc_msg;
                pcl::toROSMsg(*cloud_filtered, pc_msg);
                pointcloud_pub.publish(pc_msg);
            }
            else{
                sensor_msgs::PointCloud2 pc_msg;
                pcl::toROSMsg(*point_cloud, pc_msg);
                pointcloud_pub.publish(pc_msg);
            }

            if(publish_scan){
                sensor_msgs::PointCloud2 pc_msg2;
                sensor_msgs::LaserScan::Ptr scan_msg(new sensor_msgs::LaserScan);
                pcl::toROSMsg(*point_cloud_scan, pc_msg2);
                pointcloudToLaserscan(pc_msg2, *scan_msg);
                scan_pub.publish(scan_msg);
            }
        } else {
            VPointcloud::Ptr point_cloud(new VPointcloud());
            point_cloud->header.frame_id = frame_id;
            point_cloud->height = 1;
            point_cloud->header.stamp = static_cast<uint64_t>(sweep_end_time * 1e6);

            VPointcloud::Ptr point_cloud_scan(new VPointcloud());
            point_cloud_scan->header.frame_id = frame_id;
            point_cloud_scan->height = 1;
            point_cloud_scan->header.stamp = static_cast<uint64_t>(sweep_end_time * 1e6);
            
            {
                std::unique_lock<std::mutex> lock(pointcloud_lock);
                size_t j;
                VPoint point;
                VPoint scan_point;
                if (!sweep_data_bak->points.empty()) {
                    for (j = 0; j < sweep_data_bak->points.size(); ++j) {
                        if ((sweep_data_bak->points[j].azimuth > angle_disable_min) &&
                            (sweep_data_bak->points[j].azimuth < angle_disable_max)) {
                            continue;
                        }
                        if (scan_num == sweep_data_bak->points[j].ring) {
                            scan_point.x = sweep_data_bak->points[j].x;
                            scan_point.y = sweep_data_bak->points[j].y;
                            scan_point.z = sweep_data_bak->points[j].z;
                            scan_point.intensity = sweep_data_bak->points[j].intensity;
                            point_cloud_scan->points.push_back(scan_point);
                            ++point_cloud_scan->width;
                        }

                        point.x = sweep_data_bak->points[j].x;
                        point.y = sweep_data_bak->points[j].y;
                        point.z = sweep_data_bak->points[j].z;
                        point.intensity = sweep_data_bak->points[j].intensity;
                        point.ring = sweep_data_bak->points[j].ring;
                        point.time = sweep_data_bak->points[j].time;
                        point_cloud->points.push_back(point);
                        ++point_cloud->width;
                        current_point_time = point.time;
                        if (current_point_time - last_point_time < 0.0){
                            //ROS_WARN("timestamp is rolled back! current point time: %.12f  last point time: %.12f", current_point_time, last_point_time);
                        }
                        last_point_time = current_point_time;
                    }
                }                            
            }
            
            sensor_msgs::PointCloud2 pc_msg;
            pcl::toROSMsg(*point_cloud, pc_msg);
            pointcloud_pub.publish(pc_msg);

            if (publish_scan) {
                sensor_msgs::PointCloud2 pc_msg2;
                sensor_msgs::LaserScan::Ptr scan_msg(new sensor_msgs::LaserScan);
                pcl::toROSMsg(*point_cloud_scan, pc_msg2);
                pointcloudToLaserscan(pc_msg2, *scan_msg);
                scan_pub.publish(scan_msg);
            }
        }
        return;
    }

    void lslidarDriver::publishScan() {
        sensor_msgs::LaserScan::Ptr scan(new sensor_msgs::LaserScan);
        int layer_num_local = scan_num;
        ROS_INFO_ONCE("default channel is %d", layer_num_local);

        scan->header.frame_id = frame_id;
        scan->header.stamp = ros::Time(sweep_end_time);

        scan->angle_min = 0.0;
        scan->angle_max = 2.0 * M_PI;
        scan->angle_increment = (scan->angle_max - scan->angle_min) / point_num;

        //	scan->time_increment = motor_speed_/1e8;
        scan->range_min = min_range;
        scan->range_max = max_range;
        scan->ranges.reserve(point_num);
        scan->ranges.assign(point_num, std::numeric_limits<float>::quiet_NaN());

        scan->intensities.reserve(point_num);
        scan->intensities.assign(point_num, std::numeric_limits<float>::quiet_NaN());

        if (sweep_data->points.size() > 0) {
            for (size_t j = 0; j < sweep_data->points.size(); ++j) {
                if (layer_num_local == sweep_data->points[j].ring) {
                    float point_azimuth = sweep_data->points[j].azimuth * 0.01 * DEG_TO_RAD;
                    uint point_idx = point_azimuth / scan->angle_increment;
                    point_idx = point_idx <= point_num ? point_idx : point_idx % point_num;
                    ROS_INFO("point_idx: %d", point_idx);
                    scan->ranges[point_idx] = sweep_data->points[j].distance;
                    scan->intensities[point_idx] = sweep_data->points[j].intensity;
                }
            }
            scan_pub.publish(scan);
        }
    }

    bool lslidarDriver::lslidarC16Control(lslidar_msgs::lslidar_control::Request &req,
                                          lslidar_msgs::lslidar_control::Response &res) {
        ROS_WARN("--------------------------");
        // sleep(1);
        lslidar_msgs::LslidarPacketPtr packet0(new lslidar_msgs::LslidarPacket);
        packet0->data[0] = 0x00;
        packet0->data[1] = 0x00;
        int rc_msop = -1;

        if (req.LaserControl == 1) {

            if ((rc_msop = msop_input_->getPacket(packet0)) == 0) {
                res.status = 1;
                ROS_WARN("receive cmd: %d,already power on status", req.LaserControl);
                return true;
            }
            ROS_WARN("receive cmd: %d,power on", req.LaserControl);
            SendPacketTolidar(true);
            double time1 = ros::Time::now().toSec();

            do {
                rc_msop = msop_input_->getPacket(packet0);
                double time2 = ros::Time::now().toSec();
                if (time2 - time1 > 20) {
                    res.status = 0;
                    ROS_WARN("lidar connect error");
                    return true;
                }
            } while ((rc_msop != 0) && (packet0->data[0] != 0xff) && (packet0->data[1] != 0xee));
            sleep(5);
            res.status = 1;
        } else if (req.LaserControl == 0) {
            ROS_WARN("receive cmd: %d,power off", req.LaserControl);
            SendPacketTolidar(false);
            res.status = 1;
        } else {
            ROS_WARN("cmd error");
            res.status = 0;
        }
        return true;

    }

    bool lslidarDriver::SendPacketTolidar(bool power_switch) {
        int socketid;
        unsigned char config_data[1206];
        //int data_port = difop_data[24] * 256 + difop_data[25];
        mempcpy(config_data, difop_data, 1206);
        config_data[0] = 0xAA;
        config_data[1] = 0x00;
        config_data[2] = 0xFF;
        config_data[3] = 0x11;
        config_data[4] = 0x22;
        config_data[5] = 0x22;
        config_data[6] = 0xAA;
        config_data[7] = 0xAA;
        config_data[8] = 0x02;
        config_data[9] = 0x58;
        if (power_switch) {
            config_data[45] = 0x00;
        } else {
            config_data[45] = 0x01;
        }

        sockaddr_in addrSrv{};
        socketid = socket(2, 2, 0);
        addrSrv.sin_addr.s_addr = inet_addr(lidar_ip_string.c_str());
        addrSrv.sin_family = AF_INET;
        addrSrv.sin_port = htons(difop_udp_port);
        sendto(socketid, (const char *) config_data, 1212, 0, (struct sockaddr *) &addrSrv, sizeof(addrSrv));
        return 0;

    }

    void lslidarDriver::decodePacket(const RawPacket *packet) {
        //couputer azimuth angle for each firing
        for (size_t b_idx = 0; b_idx < BLOCKS_PER_PACKET; ++b_idx) {
            firings.firing_azimuth[b_idx] = packet->blocks[b_idx].rotation % 36000; //* 0.01 * DEG_TO_RAD;
        }
        for (size_t block_idx = 0; block_idx < BLOCKS_PER_PACKET; ++block_idx) {
            const RawBlock &raw_block = packet->blocks[block_idx];
            // computer distance ,intensity
            //      for (size_t blk_fir_idx = 0; blk_fir_idx < FIRINGS_PER_BLOCK; ++blk_fir_idx) {
            //        size_t fir_idx = blk_idx * FIRINGS_PER_BLOCK + blk_fir_idx;
            int32_t azimuth_diff_b = 0;
            if (return_mode == 1) {
                if (block_idx < BLOCKS_PER_PACKET - 1) {
                    azimuth_diff_b = firings.firing_azimuth[block_idx + 1] - firings.firing_azimuth[block_idx];
                    azimuth_diff_b = azimuth_diff_b < 0 ? azimuth_diff_b + 36000 : azimuth_diff_b;

                } else {
                    azimuth_diff_b = firings.firing_azimuth[block_idx] - firings.firing_azimuth[block_idx - 1];

                    azimuth_diff_b = azimuth_diff_b < 0 ? azimuth_diff_b + 36000 : azimuth_diff_b;
                }
            } else {
                //return mode 2
                if (block_idx < BLOCKS_PER_PACKET - 2) {
                    azimuth_diff_b = firings.firing_azimuth[block_idx + 2] - firings.firing_azimuth[block_idx];
                    azimuth_diff_b = azimuth_diff_b < 0 ? azimuth_diff_b + 36000 : azimuth_diff_b;
                } else {
                    azimuth_diff_b = firings.firing_azimuth[block_idx] - firings.firing_azimuth[block_idx - 2];

                    azimuth_diff_b = azimuth_diff_b < 0 ? azimuth_diff_b + 36000 : azimuth_diff_b;
                }

            }


            // 32 scan
            for (size_t scan_fir_idx = 0; scan_fir_idx < SCANS_PER_FIRING_CX; ++scan_fir_idx) {
                size_t byte_idx = RAW_SCAN_SIZE * scan_fir_idx;
                //azimuth
                firings.azimuth[block_idx * 32 + scan_fir_idx] = firings.firing_azimuth[block_idx] +
                                                                 scan_fir_idx * azimuth_diff_b / FIRING_TOFFSET_C8;
                firings.azimuth[block_idx * 32 + scan_fir_idx] = firings.azimuth[block_idx * 32 + scan_fir_idx] % 36000;
                // distance
                TwoBytes raw_distance{};
                raw_distance.bytes[0] = raw_block.data[byte_idx];
                raw_distance.bytes[1] = raw_block.data[byte_idx + 1];
                firings.distance[block_idx * 32 + scan_fir_idx] =
                        static_cast<double>(raw_distance.distance) * DISTANCE_RESOLUTION * distance_unit;

                //intensity
                firings.intensity[block_idx * 32 + scan_fir_idx] = static_cast<double>(
                        raw_block.data[byte_idx + 2]);
            }
        }

        return;
    }

    bool lslidarDriver::poll() {
        //ROS_INFO("lidar_number: %d",lidar_nuber_);
        // Allocate a new shared pointer for zero-copy sharing with other nodelets.
        lslidar_msgs::LslidarPacketPtr packet(new lslidar_msgs::LslidarPacket());
        // Since the rslidar delivers data at a very high rate, keep
        // reading and publishing scans as fast as possible.
        while (true) {
            int rc = msop_input_->getPacket(packet);
            if (rc == 0) break;
            if (rc < 0) return false;
        }

        // packet timestamp
        if (use_gps_ts) {
            lslidar_msgs::LslidarPacket pkt = *packet;
            if (0xff == pkt.data[1200]) {    //ptp授时
                //std::cout << "ptp";
                uint64_t timestamp_s = (pkt.data[1201] * pow(2, 32) + pkt.data[1202] * pow(2, 24) +
                                        pkt.data[1203] * pow(2, 16) +
                                        pkt.data[1204] * pow(2, 8) + pkt.data[1205] * pow(2, 0));
                uint64_t timestamp_nsce = (pkt.data[1206] * pow(2, 24) + pkt.data[1207] * pow(2, 16) +
                                           pkt.data[1208] * pow(2, 8) +
                                           pkt.data[1209] * pow(2, 0));
                timeStamp = ros::Time(timestamp_s, timestamp_nsce);// s,ns
                packet->stamp = timeStamp;
                current_packet_time = timeStamp.toSec();
            } else {          //gps授时
                memset(&cur_time, 0, sizeof(cur_time));
                cur_time.tm_year = pkt.data[1200] + 2000 - 1900;
                cur_time.tm_mon = pkt.data[1201] - 1;
                cur_time.tm_mday = pkt.data[1202];
                cur_time.tm_hour = pkt.data[1203];
                cur_time.tm_min = pkt.data[1204];
                cur_time.tm_sec = pkt.data[1205];
                packet_time_s = static_cast<uint64_t>(timegm(&cur_time)); //s
                packet_time_ns = pkt.data[1206] +
                                 pkt.data[1207] * pow(2, 8) +
                                 pkt.data[1208] * pow(2, 16) +
                                 pkt.data[1209] * pow(2, 24); //ns
                timeStamp = ros::Time(packet_time_s, packet_time_ns);
                packet->stamp = timeStamp;
                current_packet_time = timeStamp.toSec();
            }
        } else {
            packet->stamp = ros::Time::now();
            current_packet_time = packet->stamp.toSec();
        }
        if (packet->data[1210] == 0x39) {
            return_mode = 2;
        }
        ROS_INFO_ONCE("return mode: %d", return_mode);
        const RawPacket *raw_packet = (const RawPacket *) (&(packet->data[0]));

        //check if the packet is valid
        if (!checkPacketValidity(raw_packet)) return false;

        //decode the packet
        decodePacket(raw_packet);
        // find the start of a new revolution
        // if there is one, new_sweep_start will be the index of the start firing,
        // otherwise, new_sweep_start will be FIRINGS_PER_PACKET.
        size_t new_sweep_start = 0;
        do {
            if (abs(firings.azimuth[new_sweep_start] - last_azimuth) > 35000) {
                break;
            } else {
                last_azimuth = firings.azimuth[new_sweep_start];
                ++new_sweep_start;
            }
        } while (new_sweep_start < SCANS_PER_PACKET);

        // The first sweep may not be complete. So, the firings with
        // the first sweep will be discarded. We will wait for the
        // second sweep in order to find the 0 azimuth angle.
        size_t start_fir_idx = 0;
        size_t end_fir_idx = new_sweep_start;
        if (is_first_sweep && new_sweep_start == SCANS_PER_PACKET) {
            return true;
        } else {
            if (is_first_sweep) {
                is_first_sweep = false;
                start_fir_idx = new_sweep_start;
                end_fir_idx = SCANS_PER_PACKET;
                //sweep_end_time = packet->stamp.toSec() - (end_fir_idx - start_fir_idx) * 3.125 * 1e-6;
            }
        }
        for (size_t fir_idx = start_fir_idx; fir_idx < end_fir_idx; ++fir_idx) {
            if ("c32_70" == c32_type) {
                if (fir_idx % 32 == 29 || fir_idx % 32 == 6 || fir_idx % 32 == 14 || fir_idx % 32 == 22 ||
                    fir_idx % 32 == 30 || fir_idx % 32 == 7 || fir_idx % 32 == 15 || fir_idx % 32 == 23) {
//                    ROS_INFO("firings.azimuth[fir_idx] +=389;");
                    firings.azimuth[fir_idx] += 389;
                }
                if (firings.azimuth[fir_idx] > 36000) firings.azimuth[fir_idx] -= 36000;
            }

            //check if the point is valid
            if (!isPointInRange(firings.distance[fir_idx]))continue;
            //convert the point to xyz coordinate
            size_t table_idx = firings.azimuth[fir_idx];
            double cos_azimuth = cos_azimuth_table[table_idx];
            double sin_azimuth = sin_azimuth_table[table_idx];
            double x_coord, y_coord, z_coord;
            if (coordinate_opt) {
                x_coord = firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * cos_azimuth +
                          R1_ * cos((20.25 - firings.azimuth[fir_idx] * 0.01) * DEG_TO_RAD);
                y_coord = -firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * sin_azimuth +
                          R1_ * sin((20.25 - firings.azimuth[fir_idx] * 0.01) * DEG_TO_RAD);
                z_coord = firings.distance[fir_idx] * sin_scan_altitude[fir_idx % lidar_nuber_];

            } else {
                //Y-axis correspondence 0 degree
                x_coord = firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * sin_azimuth +
                          R1_ * sin((firings.azimuth[fir_idx] * 0.01 - 20.25) * DEG_TO_RAD);
                y_coord = firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * cos_azimuth +
                          R1_ * cos((firings.azimuth[fir_idx] * 0.01 - 20.25) * DEG_TO_RAD);
                z_coord = firings.distance[fir_idx] * sin_scan_altitude[fir_idx % lidar_nuber_];

            }
            // computer the time of the point
            double time;
            if (last_packet_time > 1e-6) {
                time =
                        packet->stamp.toSec() -
                        (current_packet_time - last_packet_time) * (SCANS_PER_PACKET - fir_idx - 1) / SCANS_PER_PACKET;
            } else {
                time = current_packet_time;
            }

            int remapped_scan_idx = 0;
            switch (lidar_nuber_) {
                case 1:
                    remapped_scan_idx = 0;
                    break;
                case 8:
                    remapped_scan_idx = (fir_idx % 8) % 2 * 4 + (fir_idx % 8) / 2;
                    break;
                case 16:
                    remapped_scan_idx = (fir_idx % 16) % 2 == 0 ? (fir_idx % 16) / 2 : (fir_idx % 16) / 2 + 8;
                    break;
                case 32:
                    remapped_scan_idx = (fir_idx % 32) % 4 * 8 + fir_idx % 32 / 4;
                    break;
                default:
                    remapped_scan_idx = 0;
                    break;
            }

            sweep_data->points.push_back(lslidar_msgs::LslidarPoint());
            lslidar_msgs::LslidarPoint &new_point = sweep_data->points[
                    sweep_data->points.size() - 1];
            //pack the data into point msg
            new_point.time = time;
            new_point.x = x_coord;
            new_point.y = y_coord;
            new_point.z = z_coord;
            new_point.intensity = firings.intensity[fir_idx];
            new_point.ring = remapped_scan_idx;
            new_point.azimuth = firings.azimuth[fir_idx];
            new_point.distance = firings.distance[fir_idx];
        }
        // a new sweep begins ----------------------------------------------------

        if (end_fir_idx != SCANS_PER_PACKET) {
            //publish Last frame scan
            if (last_packet_time > 1e-6) {
                sweep_end_time =
                        packet->stamp.toSec() -
                        (current_packet_time - last_packet_time) * (SCANS_PER_PACKET - end_fir_idx) / SCANS_PER_PACKET;
            } else {
                sweep_end_time = current_packet_time;
            }
            sweep_end_time = sweep_end_time > 0 ? sweep_end_time : 0;
            {
                std::unique_lock<std::mutex> lock(pointcloud_lock);
                sweep_data_bak = sweep_data;
            }
            std::thread pointcloud_pub_thread([this] { publishPointcloud(); });
            pointcloud_pub_thread.detach();

//            if (publish_scan) publishScan();
            sweep_data = lslidar_msgs::LslidarScanPtr(new lslidar_msgs::LslidarScan());

            //prepare the next frame scan
            //sweep_end_time = packet->stamp.toSec() - (end_fir_idx - start_fir_idx) * 3.125 * 1e-6;
            last_azimuth = firings.azimuth[SCANS_PER_PACKET - 1];
            start_fir_idx = end_fir_idx;
            end_fir_idx = SCANS_PER_PACKET;
            for (size_t fir_idx = start_fir_idx; fir_idx < end_fir_idx; ++fir_idx) {
                if ("c32_70" == c32_type) {
                    if (fir_idx % 32 == 29 || fir_idx % 32 == 6 || fir_idx % 32 == 14 || fir_idx % 32 == 22 ||
                        fir_idx % 32 == 30 || fir_idx % 32 == 7 || fir_idx % 32 == 15 || fir_idx % 32 == 23) {
//                    ROS_INFO("firings.azimuth[fir_idx] +=389;");
                        firings.azimuth[fir_idx] += 389;
                    }
                    if (firings.azimuth[fir_idx] > 36000) firings.azimuth[fir_idx] -= 36000;
                }

                //check if the point is valid
                if (!isPointInRange(firings.distance[fir_idx])) continue;
                //convert the point to xyz coordinate
                size_t table_idx = firings.azimuth[fir_idx];
                double cos_azimuth = cos_azimuth_table[table_idx];
                double sin_azimuth = sin_azimuth_table[table_idx];
                double x_coord, y_coord, z_coord;
                if (coordinate_opt) {
                    x_coord = firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * cos_azimuth +
                              R1_ * cos((20.25 - firings.azimuth[fir_idx] * 0.01) * DEG_TO_RAD);
                    y_coord = -firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * sin_azimuth +
                              R1_ * sin((20.25 - firings.azimuth[fir_idx] * 0.01) * DEG_TO_RAD);
                    z_coord = firings.distance[fir_idx] * sin_scan_altitude[fir_idx % lidar_nuber_];

                } else {
                    //Y-axis correspondence 0 degree
                    x_coord = firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * sin_azimuth +
                              R1_ * sin((firings.azimuth[fir_idx] * 0.01 - 20.25) * DEG_TO_RAD);
                    y_coord = firings.distance[fir_idx] * cos_scan_altitude[fir_idx % lidar_nuber_] * cos_azimuth +
                              R1_ * cos((firings.azimuth[fir_idx] * 0.01 - 20.25) * DEG_TO_RAD);
                    z_coord = firings.distance[fir_idx] * sin_scan_altitude[fir_idx % lidar_nuber_];
                }
                // computer the time of the point
                double time;
                if (last_packet_time > 1e-6) {
                    time =
                            packet->stamp.toSec() -
                            (current_packet_time - last_packet_time) * (SCANS_PER_PACKET - fir_idx - 1) /
                            SCANS_PER_PACKET;
                } else {
                    time = current_packet_time;
                }

                int remapped_scan_idx = 0;
                switch (lidar_nuber_) {
                    case 1:
                        remapped_scan_idx = 0;
                        break;
                    case 8:
                        remapped_scan_idx = (fir_idx % 8) % 2 * 4 + (fir_idx % 8) / 2;
                        break;
                    case 16:
                        remapped_scan_idx = (fir_idx % 16) % 2 == 0 ? (fir_idx % 16) / 2 : (fir_idx % 16) / 2 + 8;
                        break;
                    case 32:
                        remapped_scan_idx = (fir_idx % 32) % 4 * 8 + fir_idx % 32 / 4;
                        break;
                    default:
                        remapped_scan_idx = 0;
                        break;
                }

                sweep_data->points.push_back(lslidar_msgs::LslidarPoint());
                lslidar_msgs::LslidarPoint &new_point = sweep_data->points[
                        sweep_data->points.size() - 1];
                //pack the data into point msg
                new_point.time = time;
                new_point.x = x_coord;
                new_point.y = y_coord;
                new_point.z = z_coord;
                new_point.intensity = firings.intensity[fir_idx];
                new_point.ring = remapped_scan_idx;
                new_point.azimuth = firings.azimuth[fir_idx];
                new_point.distance = firings.distance[fir_idx];
            }
        }
        //packet_pub.publish(*packet);
        return true;
    }

    lslidarC16Driver::lslidarC16Driver(ros::NodeHandle &node, ros::NodeHandle &private_nh) : lslidarDriver(node,
                                                                                                           private_nh) {
        lidar_nuber_ = 16;
        return;
    }

    lslidarC16Driver::~lslidarC16Driver() {
        if (difop_thread_ != nullptr) {
            difop_thread_->interrupt();
            difop_thread_->join();
        }
    }

    bool lslidarC16Driver::initialize() {
        this->initTimeStamp();
        if (!loadParameters()) {
            ROS_ERROR("cannot load all required ROS parameters.");
            return false;
        }
        if (!createRosIO()) {
            ROS_ERROR("cannot create all ROS IO.");
            return false;
        }
        for (int i = 0; i < 16; ++i) {
            sin_scan_altitude[i] = sin(c16_vertical_angle[i] * DEG_TO_RAD);
            cos_scan_altitude[i] = cos(c16_vertical_angle[i] * DEG_TO_RAD);
        }

        // create the sin and cos table for different azimuth values
        for (int j = 0; j < 36000; ++j) {
            double angle = static_cast<double>(j) / 100.0 * DEG_TO_RAD;
            sin_azimuth_table[j] = sin(angle);
            cos_azimuth_table[j] = cos(angle);
        }
        angle_base = M_PI * 2 / point_num;
        return true;
    }

/** poll the device
 *  @returns true unless end of file reached
 */
    lslidarC32Driver::lslidarC32Driver(ros::NodeHandle &node, ros::NodeHandle &private_nh) : lslidarDriver(node,
                                                                                                           private_nh) {
        lidar_nuber_ = 32;
        return;
    }

    lslidarC32Driver::~lslidarC32Driver() {
        if (difop_thread_ != nullptr) {
            difop_thread_->interrupt();
            difop_thread_->join();
        }
    }

    bool lslidarC32Driver::initialize() {
        if (!loadParameters()) {
            ROS_ERROR("cannot load all required parameters.");
            return false;
        }
        if (!createRosIO()) {
            ROS_ERROR("cannot create ROS I/O.");
            return false;
        }
        if ("c32_32" == c32_type) {
            ROS_INFO("Vertical angle: 32 degrees");
            for (int i = 0; i < 32; ++i) {
                sin_scan_altitude[i] = sin(c32_vertical_angle[i] * DEG_TO_RAD);
                cos_scan_altitude[i] = cos(c32_vertical_angle[i] * DEG_TO_RAD);
            }
        } else if ("c32_70" == c32_type) {
            ROS_INFO("Vertical angle: 70 degrees");
            for (int k = 0; k < 32; ++k) {
                sin_scan_altitude[k] = sin(c32_70_vertical_angle[k] * DEG_TO_RAD);
                cos_scan_altitude[k] = cos(c32_70_vertical_angle[k] * DEG_TO_RAD);
            }
        } else if ("c32_90" == c32_type) {
            ROS_INFO("Vertical angle: 90 degrees");
            for (int k = 0; k < 32; ++k) {
                sin_scan_altitude[k] = sin(c32_90_vertical_angle[k] * DEG_TO_RAD);
                cos_scan_altitude[k] = cos(c32_90_vertical_angle[k] * DEG_TO_RAD);
            }
        }

        // create the sin and cos table for different azimuth values
        for (int j = 0; j < 36000; ++j) {
            double angle = static_cast<double>(j) / 100.0 * DEG_TO_RAD;
            sin_azimuth_table[j] = sin(angle);
            cos_azimuth_table[j] = cos(angle);
        }
        angle_base = 2 * M_PI / point_num;
        return true;
    }

    lslidarC8Driver::lslidarC8Driver(ros::NodeHandle &node, ros::NodeHandle &private_nh) : lslidarDriver(node,
                                                                                                         private_nh) {
        lidar_nuber_ = 8;
        return;
    }


    lslidarC8Driver::~lslidarC8Driver() {
        if (difop_thread_ != nullptr) {
            difop_thread_->interrupt();
            difop_thread_->join();
        }
    }

    bool lslidarC8Driver::initialize() {
        if (!loadParameters()) {
            ROS_ERROR("cannot load all required parameters.");
            return false;
        }
        if (!createRosIO()) {
            ROS_ERROR("cannot create ROS I/O.");
            return false;
        }
        for (int i = 0; i < 8; ++i) {
            sin_scan_altitude[i] = sin(c8_vertical_angle[i] * DEG_TO_RAD);
            cos_scan_altitude[i] = cos(c8_vertical_angle[i] * DEG_TO_RAD);
        }

        // create the sin and cos table for different azimuth values
        for (int j = 0; j < 36000; ++j) {
            double angle = static_cast<double>(j) / 100.0 * DEG_TO_RAD;
            sin_azimuth_table[j] = sin(angle);
            cos_azimuth_table[j] = cos(angle);
        }
        angle_base = 2 * M_PI / point_num;
        return true;
    }

    lslidarC1Driver::lslidarC1Driver(ros::NodeHandle &node, ros::NodeHandle &private_nh) : lslidarDriver(node,
                                                                                                         private_nh) {
        lidar_nuber_ = 1;
        return;
    }

    lslidarC1Driver::~lslidarC1Driver() {
        if (difop_thread_ != nullptr) {
            difop_thread_->interrupt();
            difop_thread_->join();
        }
    }

    bool lslidarC1Driver::initialize() {
        if (!loadParameters()) {
            ROS_ERROR("cannot load all required parameters.");
            return false;
        }
        if (!createRosIO()) {
            ROS_ERROR("cannot create ROS I/O.");
            return false;
        }
        for (int i = 0; i < 8; ++i) {
            sin_scan_altitude[i] = sin(c1_vertical_angle[i] * DEG_TO_RAD);
            cos_scan_altitude[i] = cos(c1_vertical_angle[i] * DEG_TO_RAD);
        }

        // create the sin and cos table for different azimuth values
        for (int j = 0; j < 36000; ++j) {
            double angle = static_cast<double>(j) / 100.0 * DEG_TO_RAD;
            sin_azimuth_table[j] = sin(angle);
            cos_azimuth_table[j] = cos(angle);
        }
        angle_base = 2 * M_PI / point_num;
        return true;
    }

}  // namespace lslidar_driver
