import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.IN)

while(1):
    if GPIO.input(22) == 0:
        os.system('sudo poweroff')
        break
    else:
        pass

GPIO.cleanup()
