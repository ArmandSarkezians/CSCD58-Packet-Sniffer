"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022
"""

class Packet(object):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def print(self):
        print(self)