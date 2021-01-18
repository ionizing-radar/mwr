#!/usr/bin/python3

import threading
import concurrent.futures
import socket
import queue
import json
import math

import RPi.GPIO as GPIO
import time

# network connection server defaults
DEFAULT_HOST = '192.168.0.205'
DEFAULT_PORT = 23500

# motor 1 setup by GPIO board pin
# at some point GPIO pins are going to be on the SCI bus
Motor1A = 31
Motor1B = 29
Motor1E = 33
# motor 2 setup
Motor2A = 13
Motor2B = 11
Motor2E = 15
# global for all the motors
MOTORS = [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]
# pulse width modulation frequency - the higher this number
MOTOR_PWM_FREQ = 100

# server socket, listens for incoming connections and then handles JSON on that socket
## the input stream should only contain JSON, otherwise it'll bork and weird things happen

def serverSocket(serverIP, serverPort, q):
	while True:
		# simple echo server
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			print ('Listening on',serverIP,':',serverPort)
			s.bind((serverIP, serverPort))
			s.listen(2)
			conn, addr = s.accept()
			# make a connection
			with conn:
				print('Connect by ', addr)
				while True:
					# get data, echo it, loop
					data = conn.recv(1024)
					if not data:
						break
					else:
						q.put(data) # enqueue data
					conn.sendall(data) # echo

def commandQueue(q):
	print("staring Q printer")
	while True:
		item = q.get()
		try:
			command = json.loads(item)
			if ("drive" in command.keys()):
				driveCommand = command.get("drive")
				r = driveCommand.get("r")
				theta = driveCommand.get("theta")
				while (theta > math.pi):
					theta -= (2*math.pi)
				while (theta < (-math.pi)):
					theta += (2*math.pi)
				if (r > 0):					
					if (theta > (math.pi/2)): # back left
						setMotor(r, math.sin(2*theta-math.pi/2), -1)
					elif (theta > 0): # forward left
						setMotor(r, 1, math.cos(2*theta))
					elif (theta > (-1 * math.pi/2)): # forward right
						setMotor(r, math.cos(2*theta), 1)
					else: # back right
						setMotor(r, -1, math.sin(2*theta-math.pi/2))
				else:
					setMotor(0,0,0)
			else:
				print(command.keys())
		except json.JSONDecodeError:
			print() # //TOOD: set motors to zero if motors non-zero and no input for 100ms

def setMotor(power, right, left):
	print ("Right: {:.2f} \tLeft: {:.5f}".format(right,left))
	#3 cases for each L-R motor: moving forwards (positive), stopped (zero), or backwards (negative)
	if (right < 0):
		pwmM1_R.start(abs(r*right)) # to absolute value this because PWM takes postive values
		pmwM1_F.stop()
	elif (right == 0):
		pwmM1_R.stop()
		pwmM1_F.stop()
	elif (right > 0):
		pwmM1_F.start(r*right)
		pwmM1_R.stop()
	if (left < 0):
		pwmM2_R.start(abs(r*left))
		pwmM2_F.stop()
	elif (left == 0):
		pwmM2_R.stop()
		pwmM2_F.stop()
	elif (left > 0):
		pwmM2_F.start(r*left)
		pwmM2_R.stop()


def initMotors():
	GPIO.setmode(GPIO.BOARD)
	# setup motor pins
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)

	# turn pins into PWM
	pwmM1_F = GPIO.PWM(Motor1A, MOTOR_PWM_FREQ) 
	pwmM1_R = GPIO.PWM(Motor1B, MOTOR_PWM_FREQ)
	pwmM2_F = GPIO.PWM(Motor2A, MOTOR_PWM_FREQ) 
	pwmM2_R = GPIO.PWM(Motor2B, MOTOR_PWM_FREQ)
	# turn all pins off
	dutyCycle = 0	
	pwmM1_F.start(dutyCycle)
	pwmM1_R.start(dutyCycle)
	pwmM2_F.start(dutyCycle)
	pwmM2_R.start(dutyCycle)

	# enable motors
	GPIO.output(Motor1E, GPIO.HIGH)
	GPIO.output(Motor2E, GPIO.HIGH)

def main():
	q = queue.Queue()
	threads = list();
	threads.append(threading.Thread(target=serverSocket, args=(DEFAULT_HOST, DEFAULT_PORT, q,)))
	threads.append(threading.Thread(target=commandQueue, args=(q,)))

	initMotors()
	
	for thread in threads:
		thread.start()


if __name__ == "__main__":
	print("starting...")
	main()

