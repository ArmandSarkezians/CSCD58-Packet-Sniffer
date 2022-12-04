export interface Packet {
  id?: number;
  name?: string;
  version?: number;
  ttl?: number;
  offset?: number;
  seq?: number;
  ack?: number;
  urg?: number;
  psh?: number;
  rst?: number;
  syn?: number;
  fin?: number;
  raw_data?: any;
  dest?: number;
  src?: number;
  protocol?: number;
}


export interface PacketTable {
  id: number;
  source: string;
  destination: string;
  sequence: number;
  protocol: string;
}
