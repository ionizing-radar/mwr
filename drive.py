import RPi.GPIO as GPIO
from Robot import Wheel
from time import sleep

# init Robot
Wheel.DEBUG = True

# init GPIO
print GPIO.RPI_INFO
GPIO.setmode(GPIO.BOARD)

# init left wheel
#	GPIO 25 (pin 22) as enable
#	GPIO 24 (pin 18) as forward
#	GPIO 23 (pin 16) as reverse

left = Wheel(22, 18, 16)

# init right wheel 
#	GPIO 11 (pin 23) as enable
#	GPIO 9 (pin 21) as forward
#	GPIO 10 (pin 19) as reverse
right = Wheel(23, 21, 19)

#right.forward()
#left.stop()

left.start()
sleep(3)
left.stop()


GPIO.cleanup()
