"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This file contains the TCP header structure.
"""

import packet

class TCP(packet):
    def ___init___(self, source, destination, length, seq, ack, urg, psh, rst, syn, fin, raw_data):
        self.source = source
        self.destination = destination
        self.length = length
        self.seq = seq
        self.ack = ack
        self.urg = urg
        self.psh = psh
        self.rst = rst
        self.syn = syn
        self.fin = fin
        self.raw_data = raw_data
    
    def __str__(self):
        print('----------TCP----------')
        print('Source Port: {}, Destination Port: {}, Sequence: {}, Length: {}'.format(self.source, self.destination, self.seq, self.length))
        print('URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN:{}'.format(self.urg, self.ack, self.psh, self.rst, self.syn, self.fin))
        print('Data: {}'.format(self.raw_data))
        print('\n')
