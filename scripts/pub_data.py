#!/usr/bin/python

import rospy
from ros_sdp.sdp_publisher import SDPPublisher

def main():
    rospy.init_node("spd_ros_pub")
    pub = SDPPublisher()
    while not rospy.is_shutdown():
        pub.step()
