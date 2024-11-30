import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    slam_launch_path = os.path.join(
        get_package_share_directory("slam_toolbox"), "launch", "online_async_launch.py"
    )
    slam_params_path = os.path.join(
        get_package_share_directory("my_robot"),
        "config",
        "mapper_params_online_async.yaml",
    )

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(slam_launch_path),
        launch_arguments={
            "slam_params_file": {slam_params_path},
            "use_sim_time": "true",
        }.items(),
    )

    return LaunchDescription([slam_launch])
