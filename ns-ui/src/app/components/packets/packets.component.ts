import { Component, OnInit } from '@angular/core';
import { PACKETS } from '../../samples/mockpackets';
import { Packet, PacketTable } from '../../models/Packet';
import { Socket } from 'ngx-socket-io';

@Component({
  selector: 'app-packets',
  templateUrl: './packets.component.html',
  styleUrls: ['./packets.component.css'],
})
export class PacketsComponent implements OnInit {
  packets = [] as PacketTable[];
  messages: any[] = [];

  constructor(private socket: Socket) {}

  ngOnInit(): void {
    this.socket.fromEvent('packets').subscribe((data: any) => {
      console.log(data);
      // push data to top of packets
      this.packets.unshift(data);
    });
  }
}
