"""
    File created by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022
"""
class Packet(dict):
    def __init__(self, raw_data, **kwargs):
        self.raw_data = raw_data
        super().__init__(**kwargs)

    def print(self):
        return self