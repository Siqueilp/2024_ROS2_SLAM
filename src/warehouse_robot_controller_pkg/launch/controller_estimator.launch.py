import os
from launch import LaunchDescription
from launch_ros.actions import Node
 
 
def generate_launch_description():
 
  return LaunchDescription([
    Node(package='warehouse_robot_controller_pkg', executable='robot1_controller',
      output='screen'),
    Node(package='warehouse_robot_controller_pkg', executable='robot1_estimator',
      output='screen'),
      Node(package='warehouse_robot_controller_pkg', executable='robot2_controller',
      output='screen'),
    Node(package='warehouse_robot_controller_pkg', executable='robot2_estimator',
      output='screen'),
  ])
