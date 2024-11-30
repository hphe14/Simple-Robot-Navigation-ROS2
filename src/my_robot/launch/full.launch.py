import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("my_robot"), "launch"),
                "/robot_rviz.launch.py",
            ]
        )
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("my_robot"), "launch"),
                "/gazebo.launch.py",
            ]
        )
    )

    xbox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("my_robot"), "launch"),
                "/xbox_contr.launch.py",
            ]
        )
    )

    return LaunchDescription(
        [
            rviz_launch,
            gazebo_launch,
            xbox_launch,
        ]
    )
