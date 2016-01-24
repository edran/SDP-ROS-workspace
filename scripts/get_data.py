#!/usr/bin/python

import rospy
from ros_sdp.sdp_subscriber import SDPSubscriber

def main():
    rospy.init_node("ros_sdp_sub")
    sub = SDPSubscriber()
    rospy.spin()

if __name__ == "__main__":
    main()
