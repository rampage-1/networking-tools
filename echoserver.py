#!/usr/bin/env python3
# ^ use user environment python3, more reliable than? /bin/python3
# for https://realpython.com/python-sockets/
# not an original work

# creates a socket object, binds it to interface:PORT, listens, accepts connection, echos back data recvd

import socket

HOST = '127.0.0.1' # loopback address for testing
PORT = 65123 # arbitrary port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# Addresss Family = AF_INET: IPv4
# SOCK_STREAM: default TCP, SOC_DGRAM: UDP
	s.bind((HOST,PORT))
	# bind associates the socket with an interface and port (for AF_INET)
	# values will differ depending on socket Address Family
	# if no HOST is specified the server will accept connections on all IPv4 interfaces
	s.listen()
	conn, addr = s.accept()
	# accept() returns a new socket object representing the connection, distinct from the listener established above
	with conn:
		print('Connection from', addr)
		while True:
			data = conn.recv(1024)
			# conn.recv() reads data sent by the client
			if not data:
				break
			conn.sendall(data)
			# echos back data recvd from client
