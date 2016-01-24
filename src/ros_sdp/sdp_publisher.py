import os
import rospy
from std_msgs.msg import String


# Don't do this in your code, mkay? :)
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)


class SDPPublisher(object):

    def __init__(self):
        self.pub = rospy.Publisher('sdp_ros_fib',
                                   String,
                                   queue_size=10)
        self.counter = 1
        self.r = rospy.Rate(1)  # Hz

    def step(self):
        nfib = fib(self.counter)
        self.pub(String("Fibonacci number #%d = %d" % (self.counter,
                                                       nfib)))
        self.counter += 1
        self.r.sleep()


def main():
    pub = SDPPublisher()
    while not rospy.is_shutdown():
        pub.step()

if __name__ == "__main__":
    main()
