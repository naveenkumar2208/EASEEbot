import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while(1):
    if GPIO.input(11) == 1:
        os.system('rosnode kill /video_recorder_first')
    else:
        pass

GPIO.cleanup()
