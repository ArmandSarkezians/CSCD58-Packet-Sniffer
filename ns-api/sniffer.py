"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the sniffer. It will sniff all 
    the packets on the network and print them out.
"""

from struct import unpack
import socket
from structures import Ethernet, IPv4, TCP, UDP, ICMP

class Sniffer():

    def __init__(self, socketio, redis_store):
        self.socketio = socketio
        self.redis_store = redis_store

    def sniff(self):
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        print("Listening for packets...\n")
        
        while True:
            raw_data, addr = s.recvfrom(65536)
            hdr = Ethernet(raw_data)
            # Protocol 8 is for IPv4
            if hdr.protocol == 8:
                ipv4 = IPv4(raw_data)

                # Protocol 1 is for ICMP
                if ipv4.protocol == 1:
                    icmp = ICMP(ipv4.raw_data)
                    self.socketio.emit('packets', icmp)
                    print(icmp)
                # Protocol 6 is for TCP
                elif ipv4.protocol == 6:
                    tcp = TCP(ipv4.raw_data)
                    self.socketio.emit('packets', tcp)
                    print(tcp)
                # Protocol 17 is for UDP
                elif ipv4.protocol == 17:
                    udp = UDP(ipv4.raw_data)
                    self.socketio.emit('packets', udp)
                    print(udp)
                # Other protocols
                else:
                    print("Other protocol: ", ipv4.protocol)
                    self.socketio.emit('packets', ipv4.protocol)
            # Other protocols
            else:
                print("Other protocol: ", hdr)
                self.socketio.emit('packets', hdr)

