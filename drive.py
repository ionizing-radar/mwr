import RPi.GPIO as GPIO
from time import sleep
from Robot import Wheel


# init Robot
Wheel.DEBUG = True

# init GPIO
print GPIO.RPI_INFO
GPIO.setmode(GPIO.BOARD)

# init left wheel
#	GPIO 13 (pin 33) as enable
#	GPIO 6 (pin 31) as forward
#	GPIO 5 (pin 29) as reverse

left = Wheel(33, 31, 29)

# init right wheel 
#	GPIO 22 (pin 15) as enable
#	GPIO 27 (pin 13) as forward
#	GPIO 17 (pin 11) as reverse
right = Wheel(15, 13, 11)

#right.forward()
#left.stop()



left.start()
right.start()
sleep(2)
left.stop()
right.stop()
left.reverse()
right.reverse()
sleep(2)
left.stop()
right.stop()



GPIO.cleanup()
