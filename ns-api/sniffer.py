"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the sniffer. It will sniff all 
    the packets on the network and print them out.
"""

from struct import unpack
import socket
from structures import ethernet, ipv4, tcp, udp, icmp

# def get_ip(addr):
#     return '.'.join(map(str, addr))


# def get_mac_addr(raw_data):
#     # Convert the MAC address into a readable format
#     bytes_str = map('{:02x}'.format, raw_data)
#     mac_addr = ':'.join(bytes_str).upper()

#     return mac_addr


# def ethr_hdr(raw_data):
#     # See CSCD58 notes for how Ethernet headers are structured

#     # Use unpack function from the struct lib to unpack ethernet headers into dest, src, and type
#     dest, src, protocol = unpack('! 6s 6s H', raw_data[:14])

#     # Convert the MAC addresses to readable format
#     dest_mac = get_mac_addr(dest)
#     src_mac = get_mac_addr(src)
#     proto = socket.htons(protocol)

#     # Get unpacked data
#     data = raw_data[14:]

#     # Data structure
#     hdr = ethernet.Ethernet(src_mac, dest_mac, proto, data)

#     return hdr


# def ip_hdr(raw_data):
#     # See CSCD58 notes for how IP headers are structured

#     # Getting the version and header length
#     ver_hdr_len = raw_data[0]
#     ver = ver_hdr_len >> 4

#     # Header length
#     hdr_len = (ver_hdr_len & 15) * 4

#     # Getting the TTL and protocol
#     ttl, protocol, src, target = unpack('! 8x B B 2x 4s 4s', raw_data[:20]) 

#     # Get data
#     data = raw_data[hdr_len:]

#     # Data structure
#     hdr = ipv4.IPv4(ver, hdr_len, ttl, protocol, get_ip(src), get_ip(target), data)

#     # Return the unpacked data
#     return hdr


# def tcp_hdr(raw_data):
#     # See CSCD58 notes for how TCP headers are structured

#     # Using unpack function to get header information
#     src_port, dest_port, seq, ack, offset_res_flg = unpack('! H H L L H', raw_data[:14])

#     # Getting flags
#     offset = (offset_res_flg >> 12) * 4
#     flag_urg = (offset_res_flg & 32) >> 5
#     flag_ack = (offset_res_flg & 16) >> 4
#     flag_psh = (offset_res_flg & 8) >> 3
#     flag_rst = (offset_res_flg & 4) >> 2
#     flag_syn = (offset_res_flg & 2) >> 1
#     flag_fin = offset_res_flg & 1

#     # Data structure
#     hdr = tcp.TCP(src_port, dest_port, offset, seq, ack, flag_urg, flag_psh, flag_rst, flag_syn, flag_fin, raw_data[offset:])

#     # Return the unpacked data
#     return hdr


# def udp_hdr(raw_data):
#     # See CSCD58 notes for how UDP headers are structured

#     # Unpack the header information
#     src_port, dest_port, size = unpack('! H H 2x H', raw_data[:8])

#     # Data structure
#     hdr = udp.UDP(src_port, dest_port, size, raw_data[8:])

#     # Return the unpacked data
#     return hdr


# def icmp_hdr(raw_data):
#     # See CSCD58 notes for how ICMP headers are structured

#     # Unpack the header information
#     icmp_type, code, checksum = unpack('! B B H', raw_data[:4])

#     # Data structure
#     hdr = icmp.ICMP(icmp_type, code, checksum, raw_data[4:])

#     # Return the unpacked data
    # return hdr

if __name__ == '__main__':
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("Listening for packets...\n")

    while True:
        raw_data, addr = s.recvfrom(65536)
        hdr = ethernet.Ethernet(raw_data)

        # Protocol 8 is for IPv4
        if hdr.protocol == 8:
            ipv4 = ipv4.IPv4(raw_data)

            # Protocol 1 is for ICMP
            if ipv4.protocol == 1:
                icmp = icmp.ICMP(ipv4.raw_data)
                print(icmp)
            
            # Protocol 6 is for TCP
            elif ipv4.protocol == 6:
                tcp = tcp.TCP(ipv4.raw_data)
                print(tcp)
            
            # Protocol 17 is for UDP
            elif ipv4.protocol == 17:
                udp = udp.UDP(ipv4.raw_data)
                print(udp)
            
            # Other protocols
            else:
                print("Other protocol: ", ipv4.protocol)
            
        # Other protocols
        else:
            print("Other protocol: ", hdr.protocol)
    

        print('------------------------------------------------------------------------------------------------------------------------')
