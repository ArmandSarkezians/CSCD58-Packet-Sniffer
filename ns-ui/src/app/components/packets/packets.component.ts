import { Component, OnInit } from '@angular/core';
import { PACKETS } from '../../samples/mockpackets';
import { Packet } from '../../models/Packet';
import { Socket } from 'ngx-socket-io';

@Component({
  selector: 'app-packets',
  templateUrl: './packets.component.html',
  styleUrls: ['./packets.component.css'],
})
export class PacketsComponent implements OnInit {
  packets = PACKETS;
  messages: any[] = [];

  constructor(private socket: Socket) {}

  ngOnInit(): void {
    this.socket.fromEvent('packets').subscribe((data: any) => {
      console.log(data);
      this.messages.push(data);
    });
  }
}
