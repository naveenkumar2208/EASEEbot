import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

while(1):
    if GPIO.input(12) == 1:
        os.system('rosnode kill /video_recorder_second')
    else:
        pass

GPIO.cleanup()
