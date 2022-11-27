"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the whois information grabber.
"""

import subprocess

result = subprocess.run(["whois", "127.0.0.1"], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))

