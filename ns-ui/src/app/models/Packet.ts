export interface Packet {
    id: number;
    source?: string;
    destination?: string;
    sequence?: number;
    ack?: number;
    protocol?: string;
    URG?: number;
    ACK?: number;
    PSH?: number;
    RST?: number;
    SYN?: number;
    FIN?: number;
    data?: string;
    size?: number;
    type?: string;
    code?: number;
    checksum?: number;
    header_length?: number;
    ttl?: number;
}