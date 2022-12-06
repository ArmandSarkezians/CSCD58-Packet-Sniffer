"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the Ethernet header structure.
"""

from .pkt import Packet
from struct import unpack
import socket
from helpers.map_ip_and_mac import get_mac_addr, get_ip

class Ethernet(Packet, dict):
    def __init__(self, raw_data):
        super().__init__(raw_data)
        dest, src, protocol = unpack('! 6s 6s H', raw_data[:14])

        self.dest = get_mac_addr(dest)
        self.src = get_mac_addr(src)
        self.protocol = socket.htons(protocol)
        self.raw_data = raw_data[14:]
        dict.__init__(self, raw_data=raw_data, dest=self.dest, src=self.src, protocol=self.protocol, name='Ethernet')

    def __str__(self):
        s = '----------Ethernet----------'
        s += 'Source: {}, Destination: {}, Protocol: {}\n'.format(self.src, self.dest, self.protocol)
        s += 'Data: {}\n'.format(self.raw_data)
        s += '\n'
        return s