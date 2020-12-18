import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 29
Motor1B = 31
Motor1E = 33

Motor2A = 11
Motor2B = 13
Motor2E = 15

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
 
print "Turning motor 1 on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(5)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
 
print "Turning motor 2 on"
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(5)

print "Stopping motor"
GPIO.output(Motor2E,GPIO.LOW)

#print "Stopping EVERYTHING"
#for pin in [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]:
#	print pin
#	GPIO.output(pin,GPIO.LOW)

#sleep(1)
#GPIO.cleanup()
