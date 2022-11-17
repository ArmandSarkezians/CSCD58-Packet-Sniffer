"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the UDP header structure.
"""

from .pkt import Packet
from struct import unpack
import socket
from helpers.map_ip_and_mac import get_mac_addr, get_ip

class UDP(Packet):
    def __init__(self, raw_data):
        super().__init__(raw_data)

        src, dest, size = unpack('! H H 2x H', raw_data[:8])

        self.src = src
        self.dest = dest
        self.length = size
        self.raw_data = raw_data
    
    def __str__(self):
        print('----------UDP----------')
        print('Source Port: {}, Destination Port: {}, Length: {}'.format(self.source, self.destination, self.length))
        print('Checksum: {}'.format(self.checksum))
        print('Data: {}'.format(self.raw_data))
        print('\n')
        return ""
