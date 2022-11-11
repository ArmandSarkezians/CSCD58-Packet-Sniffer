"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the IPv4 header structure.
"""

import packet

class IPv4(packet):
    def ___init___(self, version, length, ttl, protocol, source, destination, raw_data):
        self.version = version
        self.length = length
        self.ttl = ttl
        self.protocol = protocol
        self.source = source
        self.destination = destination
        self.raw_data = raw_data

    def __str__(self):
        print('----------IPv4----------')
        print('Version: {}, TTL: {}, Protocol: {}, Length: {},'.format(self.version, self.ttl, self.protocol, self.length))
        print('Source: {}, Destination: {}'.format(self.source, self.destination))
        print('Data: {}'.format(self.raw_data))
        print('\n')