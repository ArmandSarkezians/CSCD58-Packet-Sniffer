"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the nmap information grabber.
"""

import subprocess, re
from .arptables import get_arp_table
from structures import WhoIs

def get_nmap(ip):
    result = subprocess.run(["nmap", "-sP", ip], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8")

if __name__ == "__main__":
    print(get_nmap())
