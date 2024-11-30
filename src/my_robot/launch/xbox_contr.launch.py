from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    controller_client_node = Node(
        package="controller_inputs",
        executable="controller_clientSocket_node",
    )

    xbox_robot_control_node = Node(
        package="my_robot",
        executable="robot_control",
    )

    return LaunchDescription([xbox_robot_control_node, controller_client_node])
