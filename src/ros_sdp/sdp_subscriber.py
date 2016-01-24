import rospy
from std_msgs.msg import String


class SDPSubscriber(object):

    def __init__(self):
        self.sub = rospy.Subscriber("ros_sdp_fib",
                                    String,
                                    self.callback)

    def callback(self, data):
        rospy.loginfo("I heard %s", data.data)
