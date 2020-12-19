import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 31
Motor1B = 29
Motor1E = 33

Motor2A = 13
Motor2B = 11
Motor2E = 15

MOTORS = [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

def endit():
	for pin in MOTORS:
		#print(str(pin) + " set to GPIO.LOW")
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

def reverse():
	print("reversing")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)

def left():
	print("turning left")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.LOW)


def backleft():
	print("turning left")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.LOW)

def right():
	print("turning right")
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.LOW)

def backright():
	print("turning right")
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.LOW)	

def clockwise():
	print("turning clockwise")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)


def counterclock():
	print("turning clockwise")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)


def stop():	
	GPIO.output(MOTORS,GPIO.LOW)

def help():
	print ("RUSSELL knows how to:")
	print ("\t*drive* and *go* *forward*")
	print ("\t*reverse* and *back*")
	print ("\tturn *left* or *right* and turn *backleft* or *backright*")
	print ("\tspin *clockwise* and *counter*clockwise")
	print ("\tand *stop*")


def welcome():
	print ("██████╗░██╗░░░██╗░██████╗░██████╗███████╗██╗░░░░░")
	print ("██╔══██╗██║░░░██║██╔════╝██╔════╝██╔════╝██║░░░░░")
	print ("██████╔╝██║░░░██║╚█████╗░╚█████╗░█████╗░░██║░░░░░")
	print ("██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██╔══╝░░██║░░░░░")
	print ("██║░░██║╚██████╔╝██████╔╝██████╔╝███████╗███████╗")
	print ("╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚══════╝╚══════╝")
	print ("\nRobust Universal Survey System and Experimental Lifeform\nPress 'h' for help\n\n")


welcome()
try:
	running = True
	while running:
		command = input("> ").lower()
		if command in ["forward", "drive", "go", "yeet"]:
			forward()
		elif command in ["reverse", "back"]:
			reverse()
		elif command in ["l", "left"]:
			left()
		elif command in ["r","right"]:
			right()
		elif command in ["backleft"]:
			backleft()
		elif command in ["backright"]:
			backright()
		elif command in ["clockwise", "clock", "spinr"]:
			clockwise()
		elif command in ["counterclock", "counter", "spinl"]:
			counterclock()
		elif command in ["stop", "no", "bad", "bad russell"]:
			if command == "bad russell":
				print ("\t:(")
			stop()
		elif command in ["help", "h"]:
			help()
		elif command in ["quit", "q", "exit", "bye"]:
			running = False
		else:
			print ("RUSSELL doesn't know how to '"+command+"'\n")
except:
	endit()

endit()
