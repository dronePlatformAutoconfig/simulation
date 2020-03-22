import rospy
from std_msgs.msg import String,Bool
from random import choice, randint
import math
import time

def sim_charge():
    return round(100 * math.sin((time.time() % 100) / 100 * math.pi), 2)

def drone_station_sim():
    charge_pub = rospy.Publisher('/charge', String, queue_size=10)
    center_pub = rospy.Publisher('/center', String, queue_size=10)
    roof_pub = rospy.Publisher('/roof_state', String, queue_size=10)
    rospy.init_node('drone_station', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    center_states = ['Error', 'In process', 'Inactive']
    roof_states = ['Opened', 'Opening', 'Closing', 'Closed']
    while not rospy.is_shutdown():
        charge_pub.publish(str(sim_charge()))
        center_pub.publish(choice(center_states))
        roof_pub.publish(choice(roof_states))
        
        rate.sleep()

if __name__ == '__main__':
    try:
        drone_station_sim()
    except rospy.ROSInterruptException:
        pass