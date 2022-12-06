"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the IPv4 header structure.
"""

from structures import Ethernet
from struct import unpack
from helpers.map_ip_and_mac import get_ip

class IPv4(Ethernet, dict):
    def __init__(self, raw_data):
        super().__init__(raw_data)

        ver_hdr_len = raw_data[0]
        ver = ver_hdr_len >> 4
        hdr_len = (ver_hdr_len & 15) * 4

        ttl, protocol, src, dest = unpack('! 8x B B 2x 4s 4s', raw_data[:20])

        data = raw_data[hdr_len:]

        src = get_ip(src)
        dest = get_ip(dest)

        self.version = ver
        self.ttl = ttl
        self.protocol = protocol
        self.src = src
        self.dest = dest
        self.raw_data = data

        dict.__init__(self, version=self.version, ttl=self.ttl, protocol=self.protocol, src=self.src, dest=self.dest, raw_data=self.raw_data, name='IPv4')

    def __str__(self):
        s = '----------IPv4----------'
        s += 'Version: {}, TTL: {}, Protocol: {}\n'.format(self.version, self.ttl, self.protocol)
        s += 'Source: {}, Destination: {}\n'.format(self.src, self.dest)
        s += 'Data: {}\n'.format(self.raw_data)
        s += '\n'
        return s