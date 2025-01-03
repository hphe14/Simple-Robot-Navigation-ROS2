## Prerequisites
Ubuntu Jammy 22.04

[ROS2 Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)

[Gazebo Harmonic V 8.6.0](https://gazebosim.org/docs/harmonic/install_ubuntu/)

## Packages Required
    ros-humble-ros-gz
    ros-humble-ros-gz-bridge
    ros-humble-joint-state-publisher    
    ros-humble-xacro
    ros-humble-ros2-control
    ros-humble-navigation2 
    ros-humble-nav2-bringup
    ros-humble-slam-toolbox


## How To Run
### Main Launch File
    source install/setup.bash
    ros2 launch my_robot full.launch.py

### Using An Xbox Controller
1) Ensure you are on the same network for both Host and VM
2) Run the [controller_input.py](https://github.com/hphe14/Socket-Connection-For-Controller-inputs/blob/main/controller_input.py) Python script on host Windows PC:
    
3) Update the HOST IP in [Controller_client_inputs.py](src/controller_inputs/controller_inputs/controller_client_inputs.py) in the [controller_inputs](src/controller_inputs) package to your local IPv4 address 

![HostIPCodeSnip](https://github.com/user-attachments/assets/8e5ae707-c424-4886-87fe-ffcd513c0156)







### For SLAM Toolbox:

    ros2 launch my_robot slam.launch.py

### For Navigation (Nav2):

    ros2 launch my_robot navigation_launch.py
