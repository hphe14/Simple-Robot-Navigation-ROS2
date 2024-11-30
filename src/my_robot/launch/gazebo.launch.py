from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():

    xacro_file = os.path.join(
        get_package_share_directory("my_robot"), "urdf", "my_robot.xacro"
    )

    robot_description_config = xacro.process_file(xacro_file)

    gz_sim_launch_file = os.path.join(
        get_package_share_directory("ros_gz_sim"), "launch", "gz_sim.launch.py"
    )

    custom_world_path = os.path.join(
        get_package_share_directory("my_robot"), "worlds", "testworld.sdf"
    )

    gazebo_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gz_sim_launch_file),
        launch_arguments={
            "gz_args": [f"{custom_world_path} -v 4 -r"],
            "use_sim_time": "true",
        }.items(),
    )

    params = {
        "robot_description": robot_description_config.toxml(),
    }

    # robot state publisher node running through rviz launch node
    # robot_state_publisher_node = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     output="screen",
    #     parameters=[params],
    # )

    # robot_state_publisher_node = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     output="screen",
    #     parameters=[params],
    # )

    # joint_state_publisher_node = Node(
    #     package="joint_state_publisher",
    #     executable="joint_state_publisher",
    #     name="joint_state_publisher",
    #     parameters=[params],
    # )

    # joint_state_publisher_gui_node = Node(
    #     package="joint_state_publisher_gui",
    #     executable="joint_state_publisher_gui",
    #     name="joint_state_publisher_gui",
    #     condition=IfCondition(LaunchConfiguration("gui")),
    # )

    spawn_node = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=["-topic", "/robot_description"],
    )

    bridge_params = os.path.join(
        get_package_share_directory("my_robot"), "config", "ros_gz_bridge_params.yaml"
    )
    ros2_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "--ros-args",
            "-p",
            f"config_file:={bridge_params}",
        ],
        output="screen",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="gui",
                default_value="True",
                description="enable gui",
            ),
            gazebo_world,
            spawn_node,
            ros2_bridge,
            # robot_state_publisher_node,
            # joint_state_publisher_node,
            # joint_state_publisher_gui_node,
        ]
    )
