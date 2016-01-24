import rospy
from std_msgs.msg import String


class SDPSubscriber(object):

    def __init__(self):
        self.sub = rospy.Subscriber("sdp_ros_fib",
                                    String,
                                    self.callback)

    def callback(self, data):
        rospy.loginfo("I heard %s", data.data)
