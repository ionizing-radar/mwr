import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 29
Motor1B = 31
Motor1E = 33

Motor2A = 15
Motor2B = 13
Motor2E = 11

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

def endit():
	for pin in [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]:
		print(str(pin) + " set to GPIO.LOW")
        	GPIO.output(pin,GPIO.LOW)
	GPIO.cleanup()
	exit()

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


GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
sleep(1)
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)

try:
	running = True
	while running:
		command = raw_input("> ")
		if command == "forward" or command == "drive":
			forward()
		elif command == "stop":
			stop()
		elif command == "quit" or command == "exit":
			running = False
		else:
			stop()
except:
	endit()

endit()
