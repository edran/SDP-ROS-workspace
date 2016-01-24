cmake_minimum_required(VERSION 2.8.3)
project(ros_sdp)

find_package(catkin
  REQUIRED COMPONENTS
  rospy
  std_msgs
  cv_bridge
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS
  rospy
  std_msgs
  cv_bridge
)

install(
  DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
