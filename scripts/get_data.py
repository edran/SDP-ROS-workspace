#!/usr/bin/python

import rospy
from ros_sdp.sdp_subscriber import SDPSubscriber

def main():
    rospy.init_node("sdp_ros_sub")
    sub = SDPSubscriber()
    rospy.spin()
