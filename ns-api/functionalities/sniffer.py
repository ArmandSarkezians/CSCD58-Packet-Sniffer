"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the sniffer. It will sniff all
    the packets on the network and print them out.
"""

import socket
from structures import Ethernet, IPv4, TCP, UDP, ICMP

class Sniffer():
    def __init__(self, emitter):
        self.emitter = emitter

    def sniff(self):
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        print("Listening for packets...\n")

        table = {num:name[len("IPPROTO_"):]
          for name, num in vars(socket).items()
            if name.startswith("IPPROTO_")}

        while True:
            raw_data, _ = s.recvfrom(65536)
            hdr = Ethernet(raw_data)

            # Protocol 8 is for IPv4
            if hdr.protocol == 8:
                ip_packet = IPv4(hdr.raw_data)

                # Protocol 1 is for ICMP
                if ip_packet.protocol == 1:
                    icmp = ICMP(ip_packet.raw_data)
                    self.emitter('packets', icmp)
                    # print(icmp)

                # Protocol 6 is for TCP
                elif ip_packet.protocol == 6:
                    tcp = TCP(ip_packet.raw_data)
                    self.emitter('packets', tcp)
                    # print(tcp)

                # Protocol 17 is for UDP
                elif ip_packet.protocol == 17:
                    udp = UDP(ip_packet.raw_data)
                    self.emitter('packets', udp)
                    # print(udp)

                # Other protocols
                else:
                    pass
                    # print("Other protocol: ", table[ip_packet.protocol] if ip_packet.protocol in table else ip_packet.protocol)
                    # self.emitter('packets', table[ip_packet.protocol] if ip_packet.protocol in table else ip_packet.protocol)
            # Other protocols
            else:
                # print("Other protocol: ", table[hdr.protocol] if hdr.protocol in table else hdr.protocol)
                pass

