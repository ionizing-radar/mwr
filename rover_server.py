#!/usr/bin/env python3

import threading
import concurrent.futures
import socket
import queue
import json
import math


DEFAULT_HOST = '192.168.0.11'
DEFAULT_PORT = 23500

RIGHT_MOTOR = 0
LEFT_MOTOR = 0

# server socket, listens for incoming connections and then handles JSON on that socket
## the input stream should only contain JSON, otherwise it'll bork and weird things happen

def serverSocket(serverIP, serverPort, q):
	while True:
		# simple echo server
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			print ('Listening on',serverIP,':',serverPort)
			s.bind((serverIP, serverPort))
			s.listen()
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
	//TODO: pwm here ...



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

