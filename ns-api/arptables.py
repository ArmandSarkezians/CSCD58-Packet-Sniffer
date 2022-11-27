"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the arp table grabber.
"""

import subprocess

def get_arp_table():
    result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8")

if __name__ == "__main__":
    get_arp_table()