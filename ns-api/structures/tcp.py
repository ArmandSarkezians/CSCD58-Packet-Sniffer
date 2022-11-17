"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the TCP header structure.
"""

from .pkt import Packet
from struct import unpack
import socket
from helpers.map_ip_and_mac import get_mac_addr, get_ip

class TCP(Packet):
    def __init__(self, raw_data):
        super().__init__(raw_data)
        
        src, dest, seq, ack, offset_res_flg = unpack('! H H L L H', raw_data[:14])
        offset = (offset_res_flg >> 12) * 4
        flag_urg = (offset_res_flg & 32) >> 5
        flag_ack = (offset_res_flg & 16) >> 4
        flag_psh = (offset_res_flg & 8) >> 3
        flag_rst = (offset_res_flg & 4) >> 2
        flag_syn = (offset_res_flg & 2) >> 1
        flag_fin = offset_res_flg & 1

        self.src = src
        self.dest = dest
        self.offset = offset
        self.seq = seq
        self.ack = flag_ack
        self.urg = flag_urg
        self.psh = flag_psh
        self.rst = flag_rst
        self.syn = flag_syn
        self.fin = flag_fin
        self.raw_data = raw_data
    
    def __str__(self):
        print('----------TCP----------')
        print('Source Port: {}, Destination Port: {}, Sequence: {}, Offset: {}'.format(self.src, self.dest, self.seq, self.offset))
        print('URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN:{}'.format(self.urg, self.ack, self.psh, self.rst, self.syn, self.fin))
        print('Data: {}'.format(self.raw_data))
        print('\n')
        return ""
