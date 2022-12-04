"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the arp table grabber.
"""

"""
Address                  HWtype  HWaddress           Flags Mask            Iface
143.110.210.177          ether   fe:00:00:00:01:01   C                     eth0
143.110.214.173          ether   fe:00:00:00:01:01   C                     eth0
172.17.0.3                       (incomplete)                              docker0
143.110.222.85           ether   fe:00:00:00:01:01   C                     eth0
143.110.212.4            ether   fe:00:00:00:01:01   C                     eth0
172.17.0.2               ether   02:42:ac:11:00:02   C                     docker0
143.110.208.147          ether   fe:00:00:00:01:01   C                     eth0
143.110.213.148          ether   fe:00:00:00:01:01   C                     eth0
143.110.216.156          ether   fe:00:00:00:01:01   C                     eth0
143.110.221.41           ether   fe:00:00:00:01:01   C                     eth0
143.110.211.210          ether   fe:00:00:00:01:01   C                     eth0
mxdd030562.rna1.blindsi  ether   fe:00:00:00:01:01   C                     eth0
143.110.218.65           ether   fe:00:00:00:01:01   C                     eth0
_gateway                 ether   fe:00:00:00:01:01   C                     eth0
143.110.214.203          ether   fe:00:00:00:01:01   C                     eth0
67.207.67.3                      (incomplete)                              eth1
143.110.208.68           ether   fe:00:00:00:01:01   C                     eth0
143.110.219.141          ether   fe:00:00:00:01:01   C                     eth0
67.207.67.2                      (incomplete)                              eth1
143.110.219.140          ether   fe:00:00:00:01:01   C                     eth0
143.110.212.29           ether   fe:00:00:00:01:01   C                     eth0
143.110.215.189          ether   fe:00:00:00:01:01   C                     eth0
143.110.215.210          ether   fe:00:00:00:01:01   C                     eth0
143.110.215.90           ether   fe:00:00:00:01:01   C                     eth0
143.110.222.95           ether   fe:00:00:00:01:01   C                     eth0
windows12.gz-3           ether   fe:00:00:00:01:01   C                     eth0
143.110.218.101          ether   fe:00:00:00:01:01   C                     eth0
143.110.219.123          ether   fe:00:00:00:01:01   C                     eth0
143.110.221.169          ether   fe:00:00:00:01:01   C                     eth0
143.110.221.237          ether   fe:00:00:00:01:01   C                     eth0
143.110.218.236          ether   fe:00:00:00:01:01   C                     eth0
"""

import subprocess
import re
regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[\w.\-]*)\s+(\w*)\s+([0-9a-f:]+|\(incomplete\))\s+(\w?)\s+(\w*)"

def get_arp_table():
    result = subprocess.run(["arp"], stdout=subprocess.PIPE)
    s = result.stdout.decode("utf-8")

    matches = re.finditer(regex, s, re.MULTILINE)
    table = []
    for _, match in enumerate(matches, start=1):
        table.append({
                'ip': match.group(1),
                'hwtype': match.group(2),
                'mac': match.group(3),
                'flags': match.group(4),
                'mask': match.group(5)
            })

    return table


if __name__ == "__main__":
    print(get_arp_table())