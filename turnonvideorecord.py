import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
key = 0

while(1):
    if GPIO.input(11) == 0 and key == 0:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        os.system('rosrun image_view video_recorder_first image:=/zedm/zed_node/left/image_rect_color _filename:=videomain'+timestr+'.avi')
        key = 1
    elif GPIO.input(11) == 1 and key == 1:
        key = 0
        pass

GPIO.cleanup()
