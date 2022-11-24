#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.IN)
GPIO.setup(23,GPIO.OUT)
from nav_msgs.msg import Path
import csv
import time

def callback(msg):
    # GPIO.output(7, GPIO.HIGH)
    l = len(msg.poses)
    # print("x coordinates")
    with open('coordinates.csv','w') as file:
        writer = csv.writer(file)
        for i in range(l):
            L = [msg.poses[i].pose.position.x,msg.poses[i].pose.position.y,msg.poses[i].pose.position.z]
            # print(L)
            writer.writerow(L)
        file.close()

    x = GPIO.input(19)
    if x == 0:
        GPIO.output(23,GPIO.HIGH)
        # time.sleep(1)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open('coordinates'+timestr+'.csv','w') as file:
            writer = csv.writer(file)
            for i in range(l):
                L = [msg.poses[i].pose.position.x,msg.poses[i].pose.position.y,msg.poses[i].pose.position.z]
                # print(L)
                writer.writerow(L)
            file.close()
        # print(timestr)
        GPIO.output(23,GPIO.LOW)
    # GPIO.output(7, GPIO.LOW)
    # time.sleep(1);
        # print(msg.poses[i].pose.position.x)
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", l)
    # msg.poses[2:].pose.position.x

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('positionaltrack', anonymous=False)

    rospy.Subscriber("zedm/zed_node/path_map", Path, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        # pass
        with open('coordinates.csv','a') as file:
            file.close()
            GPIO.cleanup()
        # with open('coordinates.csv','w') as file:
        #     writer = csv.writer(file)
        #    for i in range(l):
        #        L = [msg.poses[i].pose.position.x,msg.poses[i].pose.position.y,msg.poses[i].pose.position.z]
        #        print(L)
        #        writer.writerow(L)
    
   #         file.close()        
