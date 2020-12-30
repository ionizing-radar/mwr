#!/usr/bin/env python3

import socket

# get HOST ip from ionizing-radar.ca/russel.ip
HOST = '192.168.0.11'
PORT = 23500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	print ('Listening on',HOST,':',PORT)
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connect by ', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)