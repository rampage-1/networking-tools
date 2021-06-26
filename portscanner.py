#!/usr/bin/env python3
# for https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course
# not an original work

# a terrible port scanner, a functional port scanner

import sys
import socket
from datetime import datetime

# usage: ./portscanner.py <IPv4 Address>
# args 0 and 1, len(argv) == 2, argv[1] = hostname/IP address

# handle arg count
if len(sys.argv) != 2:
    print("usage: ./portscanner.py <IPv4 Address>")
    sys.exit() # exit without Traceback
else:
    try:
        target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
    except socket.gaierror:
	# handle exception where name or service is not known
        print("\nhostname could not be resolved")
        sys.exit()

# print banner
print("_" * 50)
print("\nstarted: " + str(datetime.now()))
print("\nscanning target: " + target)
print("_" * 50)

try:
    for port in range(50, 55):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print("port {} is open".format(port))
            else:
                print("port {} is not open".format(port))
            s.close()

except KeyboardInterrupt:
	print("\nexiting")
	sys.exit()

except socket.error:
	print("\ncould not connect")
	sys.exit()
