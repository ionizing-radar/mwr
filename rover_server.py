#!/usr/bin/env python3

import threading
import socket
import json


DEFAULT_HOST = '192.168.0.11'
DEFAULT_PORT = 23500

# server socket, listens for incoming connections and then handles JSON on that socket
## the input stream should only contain JSON, otherwise it'll bork and weird things happen

def serverSocket(serverIP, serverPort):
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
						try:
							print(data.decode("utf-8"))
						except KeyError:
							print("not a JSON")
	                              
					conn.sendall(data)
					print("")

def main():
	threading.Thread(target=serverSocket(DEFAULT_HOST, DEFAULT_PORT))

if __name__ == "__main__":
	print("starting")
	main()

