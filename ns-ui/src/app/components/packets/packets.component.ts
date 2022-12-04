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

  update = true;
  options = [{l: 'On', v: true}, {l: 'Off', v: false}]

  constructor(private socket: Socket) {}

  ngOnInit(): void {
    this.socket.fromEvent('packets').subscribe((data: any) => {
      if (this.update) {
        console.log(data);
        this.packets.unshift(data);
      }
    });
  }

  clickedItem(_t12: any) {
    throw new Error('Method not implemented.');
  }

  toggleUpdating(event: any) {
    console.log(event);
    this.update = event.value;
  }
}
