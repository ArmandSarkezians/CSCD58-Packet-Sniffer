"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the arp table grabber.
"""

import subprocess

result = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))