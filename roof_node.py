#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String,Bool

def talker():
    RoofIsOpen = True
    pub = rospy.Publisher('Roofchatter', Bool, queue_size=10)
    rospy.init_node('Rooftalker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if RoofIsOpen == True:
            RoofIsOpen = False
        else:
            RoofIsOpen = True
        pub.publish(RoofIsOpen)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
