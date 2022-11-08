"""
    Made by Ahmed Halat, Armand Sarkezians, and Mohamed Halat
    CSCD58 Fall 2022

    This is the main file for the sniffer. It will sniff all 
    the packets on the network and print them out.
"""

from struct import unpack
import socket


def get_ip(addr):
    return '.'.join(map(str, addr))


def get_mac_addr(raw_data):
    # Convert the MAC address into a readable format
    bytes_str = map('{:02x}'.format, raw_data)
    mac_addr = ':'.join(bytes_str).upper()

    return mac_addr


def ethr_hdr(raw_data):
    # See CSCD58 notes for how Ethernet headers are structured

    # Use unpack function from the struct lib to unpack ethernet headers into dest, src, and type
    dest, src, protocol = unpack('! 6s 6s H', raw_data[:14])

    # Convert the MAC addresses to readable format
    dest_mac = get_mac_addr(dest)
    src_mac = get_mac_addr(src)
    proto = socket.htons(protocol)

    # Return the unpacked data
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data 


def ip_hdr(raw_data):
    # See CSCD58 notes for how IP headers are structured

    # Getting the version and header length
    ver_hdr_len = raw_data[0]
    ver = ver_hdr_len >> 4

    # Header length
    hdr_len = (ver_hdr_len & 15) * 4

    # Getting the TTL and protocol
    ttl, protocol, src, target = unpack('! 8x B B 2x 4s 4s', raw_data[:20]) 

    # Get data
    data = raw_data[hdr_len:]

    # Return the unpacked data
    return ver, hdr_len, ttl, protocol, get_ip(src), get_ip(target), data


def tcp_hdr(raw_data):
    # See CSCD58 notes for how TCP headers are structured

    # Using unpack function to get header information
    src_port, dest_port, seq, ack, offset_res_flg = unpack('! H H L L H', raw_data[:14])

    # Getting flags
    offset = (offset_res_flg >> 12) * 4
    flag_urg = (offset_res_flg & 32) >> 5
    flag_ack = (offset_res_flg & 16) >> 4
    flag_psh = (offset_res_flg & 8) >> 3
    flag_rst = (offset_res_flg & 4) >> 2
    flag_syn = (offset_res_flg & 2) >> 1
    flag_fin = offset_res_flg & 1

    # Return the unpacked data
    return src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, raw_data[offset:]


def udp_hdr(raw_data):
    # See CSCD58 notes for how UDP headers are structured

    # Unpack the header information
    src_port, dest_port, size = unpack('! H H 2x H', raw_data[:8])

    # Return the unpacked data
    return src_port, dest_port, size, raw_data[8:]


def icmp_hdr(raw_data):
    # See CSCD58 notes for how ICMP headers are structured

    # Unpack the header information
    icmp_type, code, checksum = unpack('! B B H', raw_data[:4])

    # Return the unpacked data
    return icmp_type, code, checksum, raw_data[4:]


if __name__ == '__main__':
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("Listening for packets...\n")

    while True:
        raw_data, addr = s.recvfrom(65536)
        dest_mac, src_mac, proto, data = ethr_hdr(raw_data)
        print('Destination MAC: {}, Source MAC: {}, Type: {}'.format(dest_mac, src_mac, proto))
        print('\n')

        # Protocol 8 is for IPv4
        if proto == 8:
            ipv4 = ip_hdr(data)
            print('IPv4\nVersion: {}, Header Length: {}, TTL: {}, Protocol: {}, Source: {}, Target: {}'.format(ipv4[0], ipv4[1], ipv4[2], ipv4[3], ipv4[4], ipv4[5]))
            print('Data: {}'.format(ipv4[6]))
            print('\n')

        # Protocol 6 is for TCP
        if ipv4[3] == 6:
            src_port, dest_port, seq, ack, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_hdr(data)
            print('TCP\nSource Port: {}, Destination Port: {}, Sequence: {}, Acknowledgement: {}'.format(src_port, dest_port, seq, ack))
            print('URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN:{}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
            print('Data: {}'.format(data))
            print('\n')

        # Protocol 1 is for ICMP
        elif ipv4[3] == 1:
            icmp_type, code, checksum, data = icmp_hdr(data)
            print('ICMP\nType: {}, Code: {}, Checksum: {}'.format(icmp_type, code, checksum))
            print('Data: {}'.format(data))
            print('\n')
        
        # Protocol 17 is for UDP
        elif ipv4[3] == 17:
            src_port, dest_port, size, data = udp_hdr(data)
            print('UDP \nSource Port: {}, Destination Port: {}, Size: {}'.format(src_port, dest_port, size))
            print('Data: {}'.format(data))
            print('\n')
