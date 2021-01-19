#!/usr/bin/python3

import threading
import concurrent.futures
import socket
import queue
import json
import math

import RPi.GPIO as GPIO
import time

from MotorController import MotorController

# network connection server defaults
DEFAULT_HOST = '192.168.0.205'
DEFAULT_PORT = 23500

# server socket, listens for incoming connections and then handles JSON on that socket
## the input stream should only contain JSON, otherwise it'll bork and weird things happen
def serverSocket(serverIP, serverPort, q):
	while True:
		# simple echo server
		try:
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
		except KeyboardInterrupt:
			conn.close()

def commandQueue(q):

	print("initiallzing MotorController")
	Motor1A = 31
	Motor1B = 29
	Motor1E = 33
	Motor2A = 13
	Motor2B = 11
	Motor2E = 15
	drive = MotorController(Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E)
	drive.stop()

	print("staring Q parser")
	while True:
		item = q.get().decode("utf-8")
		try:
			command = json.loads(item)
			if ("drive" in command.keys()):
				driveCommand = command.get("drive")
				print(driveCommand)
				r = driveCommand.get("r")
				theta = driveCommand.get("theta")
				while (theta > math.pi):
					theta -= (2*math.pi)
				while (theta < (-math.pi)):
					theta += (2*math.pi)
				if (r > 0):					
					if (theta > (math.pi/2)): # back left
						drive.setMotor(r, math.sin(2*theta-math.pi/2), -1)
					elif (theta > 0): # forward left
						drive.setMotor(r, 1, math.cos(2*theta))
					elif (theta > (-1 * math.pi/2)): # forward right
						drive.setMotor(r, math.cos(2*theta), 1)
					else: # back right
						drive.setMotor(r, -1, math.sin(2*theta-math.pi/2))
				else:
					drive.setMotor(0,0,0)
			else:
				print("command.keys(): "+command.keys())
		except TypeError:
			print("TypeError with json input:")
			print(item)
		except ValueError:
			print("ValueError with json input:")
			print(item)

		# //TOOD: set motors to zero if motors non-zero and no input for 100ms

def main():
	
	q = queue.Queue()

	threads = list();
	threads.append(threading.Thread(target=serverSocket, args=(DEFAULT_HOST, DEFAULT_PORT, q,)))
	threads.append(threading.Thread(target=commandQueue, args=(q,)))


	
	for thread in threads:
		thread.start()

if __name__ == "__main__":
	print("starting...")
	main()

