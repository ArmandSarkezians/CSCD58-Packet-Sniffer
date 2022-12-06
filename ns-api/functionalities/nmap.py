"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the nmap information grabber.
"""

import subprocess
from .whois import get_whois

def get_nmap():
    ip_tuple = get_whois()[0].cidr[0]
    ip = ip_tuple[0]
    ip = ip.split(".")
    ip[-1] = "1"
    ip = ".".join(ip)
    ip+="/24"

    result = subprocess.run(["nmap", "-sL", ip], stdout=subprocess.PIPE)

    return result.stdout.decode("utf-8")

if __name__ == "__main__":
    print(get_nmap())
