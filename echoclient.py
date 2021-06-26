#!/usr/bin/env python3
# for https://realpython.com/python-sockets/
# not an original work

# creates socket object, connects to HOST:PORT, sends a msg, prints the reply

import socket

HOST = '127.0.0.1' # loopback address for testing
PORT = 65123 # arbitrary port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello, Echo Server!')
	data = s.recv(1024)
	# 1024 is a buffer size

print('Received', repr(data))
