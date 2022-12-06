"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the TCP header structure.
"""

from structures import IPv4
from struct import unpack
import socket
from helpers.map_ip_and_mac import get_mac_addr, get_ip

class TCP(IPv4, dict):
    def __init__(self, raw_data):
        super().__init__(raw_data)

        src_port, dest_port, seq, ack, offset_res_flg = unpack('! H H L L H', raw_data[:14])
        offset = (offset_res_flg >> 12) * 4
        flag_urg = (offset_res_flg & 32) >> 5
        flag_ack = (offset_res_flg & 16) >> 4
        flag_psh = (offset_res_flg & 8) >> 3
        flag_rst = (offset_res_flg & 4) >> 2
        flag_syn = (offset_res_flg & 2) >> 1
        flag_fin = offset_res_flg & 1

        self.src_port = src_port
        self.dest_port = dest_port
        self.offset = offset
        self.seq = seq
        self.ack = flag_ack
        self.urg = flag_urg
        self.psh = flag_psh
        self.rst = flag_rst
        self.syn = flag_syn
        self.fin = flag_fin
        self.raw_data = raw_data

        dict.__init__(self, raw_data=raw_data, src=self.src, dest=self.dest, src_port=self.src_port, dest_port=self.dest_port, offset=self.offset, seq=self.seq, ack=self.ack, urg=self.urg, psh=self.psh, rst=self.rst, syn=self.syn, fin=self.fin, name='TCP')

    def __str__(self):
        s = '----------TCP----------\n'
        s += 'Source: {}, Destination: {}\n'.format(self.src, self.dest)
        s += 'Source Port: {}, Destination Port: {}, Sequence: {}, Offset: {}\n'.format(self.src_port, self.dest_port, self.seq, self.offset)
        s += 'URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN:{}\n'.format(self.urg, self.ack, self.psh, self.rst, self.syn, self.fin)
        s += 'Data: {}\n'.format(self.raw_data)
        s += '\n'
        return s
