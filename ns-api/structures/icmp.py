"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the ICMP header structure.
"""

from .pkt import Packet
from struct import unpack
import socket
from helpers.map_ip_and_mac import get_mac_addr, get_ip

class ICMP(Packet):
    def __init__(self, raw_data):
        super().__init__(raw_data)

        type, code, checksum = unpack('! B B H', raw_data[:4])
        
        self.type = type
        self.code = code
        self.checksum = checksum
        self.raw_data = raw_data

    def __str__(self):
        print('----------ICMP----------')
        print('Type: {}, Code: {}, Checksum: {}'.format(self.type, self.code, self.checksum))
        print('Data: {}'.format(self.raw_data))
        print('\n')
        return ""