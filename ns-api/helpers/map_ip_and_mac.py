def get_ip(addr):
    return '.'.join(map(str, addr))


def get_mac_addr(raw_data):
    # Convert the MAC address into a readable format
    bytes_str = map('{:02x}'.format, raw_data)
    mac_addr = ':'.join(bytes_str).upper()

    return mac_addr