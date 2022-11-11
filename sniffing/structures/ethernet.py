"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the IPv4 header structure.
"""

import packet

class Ethernet(packet):
    def ___init___(self, src, dest, protocol, raw_data):
        self.src = src
        self.dest = dest
        self.protocol = protocol
        self.raw_data = raw_data

    def __str__(self):
        print('----------Ethernet----------')
        print('Source: {}, Destination: {}, Protocol: {}'.format(self.src, self.dest, self.protocol))
        print('Data: {}'.format(self.raw_data))
        print('\n')