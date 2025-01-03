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
    source install/setup.bash
    ros2 launch my_robot full.launch.py


To use xbox controller, run [this](https://github.com/hphe14/Socket-Connection-For-Controller-inputs/blob/main/controller_input.py) python script on host windows pc:
    
Change HOST IP in Controller_client_inputs.py in the controller_inputs package to local ipv4 address 
![399980301-a5b65bb3-5bc3-4746-8bac-7cde10dc16e8](https://github.com/user-attachments/assets/cd5073fa-15bf-4209-b936-0b2c28963c04)




For Slam Toolbox:

    ros2 launch my_robot slam.launch.py

For Nav2:

    ros2 launch my_robot navigation_launch.py
