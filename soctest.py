#!/bin/python3
# for https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course
# not an original work

# Sets up a short-lived TCP socket to HOST:PORT 

import socket

HOST = '127.0.0.1' # loopback address for testing
PORT = 7777 # arbitrary port

# very common to this type of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: IPv4, SOCK_STREAM: default TCP
# SOC_DGRAM: UDP

s.connect((HOST, PORT))
