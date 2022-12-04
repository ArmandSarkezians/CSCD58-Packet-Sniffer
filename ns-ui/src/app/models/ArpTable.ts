export interface ArpTableRow {
  ip: string;
  hwtype: string;
  mac: string;
  flags: string;
  mask: string;
}

export type ArpTable = ArpTableRow[];
