import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.IN)

while(1):
    if GPIO.input(15) == 0:
        os.system('roslaunch zed_wrapper zedm.launch')
    else:
        pass

GPIO.cleanup()