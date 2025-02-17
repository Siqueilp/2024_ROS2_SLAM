# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
"""
Demo for spawn_entity.
Launches Gazebo and spawns a model
"""
# A bunch of software packages that are needed to launch ROS2
import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir,LaunchConfiguration,PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
 
def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    paused = LaunchConfiguration('paused', default='true')
    world_file_name = 'warehouse.world'
    pkg_dir = get_package_share_directory('warehouse_robot_spawner_pkg')
 
    os.environ["GAZEBO_MODEL_PATH"] = os.path.join(pkg_dir, 'models')
 
    world = os.path.join(pkg_dir, 'worlds', world_file_name)
    launch_file_dir = os.path.join(pkg_dir, 'launch')
 
    gazebo = ExecuteProcess(
            cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_init.so', 
            '-s', 'libgazebo_ros_factory.so'],
            output='screen')
 
    #GAZEBO_MODEL_PATH has to be correctly set for Gazebo to be able to find the model
    #spawn_entity = Node(package='gazebo_ros', node_executable='spawn_entity.py',
    #                    arguments=['-entity', 'demo', 'x', 'y', 'z'],
    #                    output='screen')
    spawn_entity1 = Node(package='warehouse_robot_spawner_pkg', executable='spawn_demo1',
                        arguments=['WarehouseBot1', 'demo', '-1.5', '-4.0', '0.0'],
                        output='screen')
    #spawn_entity2 = Node(package='warehouse_robot_spawner_pkg', executable='spawn_demo2',
    #                    arguments=['WarehouseBot2', 'demo', '1.5', '1.5', '0.0'],
    #                    output='screen')
    
    #SLAM Toolbox Utilization
    slam_launch = IncludeLaunchDescription(
    	PythonLaunchDescriptionSource([
    		PathJoinSubstitution([FindPackageShare('slam_toolbox'),'launch','online_async_launch.py'])
    	]),
    	launch_arguments={
    	
    'slam_params_file':PathJoinSubstitution([FindPackageShare('warehouse_robot_spawner_pkg'),'config','mapper_params_online_async.yaml']),
    	'use_sim_time':'true'
    	}.items()
    )
    
    #Start RVIZ
#    rviz_node = Node(
#    	package='rviz2',
#    	executable='rviz2',
#    	name='rviz2',
#    	output='screen',
#  	arguments=['-d', PathJoinSubstitution([
#   		FindPackageShare('warehouse_robot_spawner_pkg'),
#   		'config',
#   		'slam_config.rviz'
#   	])]
#   )
 
    return LaunchDescription([
        gazebo,
        spawn_entity1,
#        spawn_entity2,
        slam_launch,
#        rviz_node,
    ])
