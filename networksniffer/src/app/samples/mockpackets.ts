import { Packet } from '../models/Packet'

export const PACKETS: Packet[] = [
    {
        "id": 1,
        "source": "1.1.1.1",
        "destination": "2.2.2.2",
        "sequence": 1,
        "ack": 1,
        "protocol": "TCP",
        "URG": 0,
        "ACK": 1,
        "PSH": 0,
        "RST": 0,
        "SYN": 1,
        "FIN": 0,
        "data": "",
    },
    {
        "id": 2,
        "source": "3.3.3.3",
        "destination": "4.4.4.4",
        "size": 100,
        "protocol": "UDP",
        "data": "",
    },
    {
        "id": 3,
        "protocol": "ICMP",
        "type": "Echo Request",
        "code": 0,
        "checksum": 0,
        "data": "",
    },
    {
        "id": 4,
        "header_length": 5,
        "ttl": 64,
        "protocol": "IPv4",
        "source": "7.7.7.7",
        "destination": "8.8.8.8",
        "data": "",
    },
];