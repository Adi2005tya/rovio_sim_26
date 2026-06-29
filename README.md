Steps to run the Simulation:

Step1: 
  clone the repo in your ros2_ws or in any other workspace

Step2:
  source your workspace with

  source ~/ros2_ws/install/setup.bash

Step3:

  colcon build

Step4: 
  use the below given command to launch the Stonefish simulation.

  ros2 launch stonefish_ros2 stonefish_simulator.launch.py \
  scenario_desc:=$(pwd)/ros2_ws/src/stonefish_ros2/resources/scenes/floating_box.scn

  here change the directory according to your folders!!

Done. You will see box floating in Ocean.


Update:
  
  1)For simlation of ROV bot, currently we will go with urdf_v1_old.scn flie.
  2)Menton this urdf_v1__old.scn in the launch file of urdf_v1.launch.py
  3)Open the urdf_v1_old.scn file and add the material in base link -  <material name="Neutral"/>
  4) Colcon Build and follow the below steps.
  
  how to test the thruster:
    ros2 topic pub --rate 10 /rovio/thrusters/command std_msgs/msg/Float64MultiArray "{data: [10,0,0,0,0,0,0,10]}"   
    the values may differ
  how to launch?
    ros2 launch stonefish_ros2 urdf_v1.launch.py

  urdf_v2 is the current used urdf as it follows x axis for thruster axis. urdf_v1_old.scn is the current working scene file
  


Update:
  how to test the thruster:
    ros2 topic pub --rate 10 /rovio/thrusters/command std_msgs/msg/Float64MultiArray "{data: [10,0,0,0,0,0,0,10]}"   
    the values may differ
  how to launch?
    ros2 launch stonefish_ros2 urdf_v1.launch.py

  urdf_v2 is the current used urdf as it follows x axis for thruster axis. urdf_v1_old.scn is the current working scene file
  

