"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the UDP header structure.
"""

from structures import IPv4
from struct import unpack
import socket
from helpers.map_ip_and_mac import get_mac_addr, get_ip

class UDP(IPv4, dict):
    def __init__(self, raw_data):
        super().__init__(raw_data)

        src_port, dest_port, size = unpack('! H H 2x H', raw_data[:8])

        self.src_port = src_port
        self.dest_port = dest_port
        self.length = size
        self.raw_data = raw_data

        dict.__init__(self, raw_data=raw_data, src=self.src, dest=self.dest, src_port=self.src_port, dest_port=self.dest_port, length=self.length, name='UDP')

    def __str__(self):
        s = '----------UDP----------\n'
        s += 'Source: {}, Destination: {}\n'.format(self.src, self.dest)
        s += 'Source Port: {}, Destination Port: {}, Length: {}\n'.format(self.src_port, self.dest_port, self.length)
        s += 'Data: {}\n'.format(self.raw_data)
        s += '\n'
        return s
