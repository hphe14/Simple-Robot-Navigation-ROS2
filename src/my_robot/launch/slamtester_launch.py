import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time")
    slam_params_file = LaunchConfiguration("slam_params_file")

    declare_use_sim_time_argument = DeclareLaunchArgument(
        "use_sim_time", default_value="true", description="Use simulation/Gazebo clock"
    )
    declare_slam_params_file_cmd = DeclareLaunchArgument(
        "slam_params_file",
        default_value=os.path.join(
            get_package_share_directory("my_robot"),
            "config",
            "mapper_params_online_async.yaml",
        ),
        description="Full path to the ROS2 parameters file to use for the slam_toolbox node",
    )

    # has_node_params = HasNodeParams(source_file=slam_params_file,
    #                                 node_name='slam_toolbox')

    # actual_params_file = PythonExpression(['"', slam_params_file, '" if ', has_node_params,
    #                                     ' else "', default_params_file, '"'])

    # log_param_change = LogInfo(msg=['provided params_file ',  slam_params_file,
    #                                 ' does not contain slam_toolbox parameters. Using default: ',
    #                                 default_params_file],
    #                         condition=UnlessCondition(has_node_params))

    start_async_slam_toolbox_node = Node(
        parameters=[slam_params_file, {"use_sim_time": use_sim_time}],
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        name="slam_toolbox",
        output="screen",
    )

    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_slam_params_file_cmd)
    ld.add_action(start_async_slam_toolbox_node)

    return ld
