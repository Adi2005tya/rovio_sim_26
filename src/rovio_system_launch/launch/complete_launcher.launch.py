from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    # Get package paths
    stonefish_ros2_pkg = FindPackageShare('stonefish_ros2')
    teleop_rovio_pkg = FindPackageShare('teleop_rovio')
    
    # Include sim launcher
    sim_launcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([stonefish_ros2_pkg, 'launch', 'sim_launcher.launch.py'])
        )
    )
    
    # Include teleop launcher
    teleop_launcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([teleop_rovio_pkg, 'launch', 'teleop_rovio.launch.py'])
        )
    )
    
    return LaunchDescription([
        sim_launcher,
        teleop_launcher
    ])
