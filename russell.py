import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 31
Motor1B = 29
Motor1E = 33

Motor2A = 13
Motor2B = 11
Motor2E = 15

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

def forward():
	print("driving forwards")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

def stop():	
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)


running = True

while running:
	command = raw_input("> ")
	print(command)
	if ((command == "forward") or (command == "drive")):
		forward()
	elif command == "stop":
		stop()
	elif command == "quit":
		running = False
	else:
		stop()



#sleep(1)
#GPIO.cleanup() ## WWWHYYY!!!!
