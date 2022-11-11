"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the IPv4 header structure.
"""

import packet

class ICMP(packet):
    def ___init___(self, type, code, checksum, raw_data):
        self.type = type
        self.code = code
        self.checksum = checksum
        self.raw_data = raw_data

    def __str__(self):
        print('----------ICMP----------')
        print('Type: {}, Code: {}, Checksum: {}'.format(self.type, self.code, self.checksum))
        print('Data: {}'.format(self.raw_data))
        print('\n')