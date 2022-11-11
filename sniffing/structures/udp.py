"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the UDP header structure.
"""

import packet

class UDP(packet):
    def ___init___(self, source, destination, length, checksum, raw_data):
        self.source = source
        self.destination = destination
        self.length = length
        self.checksum = checksum
        self.raw_data = raw_data
    
    def __str__(self):
        print('----------UDP----------')
        print('Source Port: {}, Destination Port: {}, Length: {}'.format(self.source, self.destination, self.length))
        print('Checksum: {}'.format(self.checksum))
        print('Data: {}'.format(self.raw_data))
        print('\n')
