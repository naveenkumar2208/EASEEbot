import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.IN)

while(1):
    if GPIO.input(19) == 0:
        os.system('rosnode kill -a')
    else:
        pass

GPIO.cleanup()
