from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time")

    # looking for rviz config and xacro file
    rvizConfigPath = os.path.join(
        get_package_share_directory("my_robot"), "config", "robot_config.rviz"
    )
    xacro_file = os.path.join(
        get_package_share_directory("my_robot"), "urdf", "my_robot.xacro"
    )

    robot_description_config = xacro.process_file(xacro_file)
    params = {
        "robot_description": robot_description_config.toxml(),
    }

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params, {"use_sim_time": True}],
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        parameters=[params, {"use_sim_time": True}],
    )

    # joint_state_publisher_gui_node = Node(
    #     package="joint_state_publisher_gui",
    #     executable="joint_state_publisher_gui",
    #     name="joint_state_publisher_gui",
    #     condition=IfCondition(LaunchConfiguration("gui")),
    # )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rvizConfigPath],
        parameters=[{"use_sim_time": True}],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Use sim time if true",
            ),
            robot_state_publisher_node,
            joint_state_publisher_node,
            # joint_state_publisher_gui_node,
            rviz_node,
        ]
    )
