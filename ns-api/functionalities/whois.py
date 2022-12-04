"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the whois information grabber.
"""

import subprocess, re
from .arptables import get_arp_table
from structures import WhoIs

def get_ips():
    result = get_arp_table()
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", result)
    return ips


def get_whois():
    ips = get_ips()
    for item in ips:
        result = subprocess.run(["whois", item], stdout=subprocess.PIPE)
        data = result.stdout.decode("utf-8")
        whois = WhoIs(data)
        return whois

if __name__ == "__main__":
    print(get_whois())
