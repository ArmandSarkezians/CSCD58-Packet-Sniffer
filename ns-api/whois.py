"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the whois information grabber.
"""

import subprocess
import arptables
import re

def get_ips():
    result = arptables.get_arp_table()
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", result)
    return ips
        

def whois(ips):
    for item in ips:
        result = subprocess.run(["whois", item], stdout=subprocess.PIPE)
        return result.stdout.decode("utf-8")

if __name__ == "__main__":
    ips = get_ips()
    whois(ips)
