import { Component, OnInit } from '@angular/core';
import { PACKETS } from '../../samples/mockpackets';
import { Packet, PacketTable } from '../../models/Packet';
import { Socket } from 'ngx-socket-io';
import { DialogService } from 'primeng/dynamicdialog';
import { PacketItemComponent } from '../packet-item/packet-item.component';

@Component({
  selector: 'app-packets',
  templateUrl: './packets.component.html',
  styleUrls: ['./packets.component.css'],
  providers: [DialogService],
})
export class PacketsComponent implements OnInit {
  packets = [] as PacketTable[];
  messages: any[] = [];

  MAX_PACKETS = 300;

  update = true;
  options = [{l: 'On', v: true}, {l: 'Off', v: false}]

  constructor(
    private socket: Socket,
    public dialogService: DialogService
  ) {}

  ngOnInit(): void {
    this.socket.fromEvent('packets').subscribe((data: any) => {
      if (this.update) {
        console.log(data);
        this.packets.unshift(data);

        if (this.packets.length > this.MAX_PACKETS) {
          // remove 100 packets
          this.packets.splice(this.MAX_PACKETS - 100, 100);
        }
      }
    });
  }

  clickedItem(packet: Packet) {
    console.log(packet);
    const ref = this.dialogService.open(PacketItemComponent, {
      data: { packet },
      header: 'Packet',
      width: '70%',
    });
  }

  toggleUpdating(event: any) {
    console.log(event);
    this.update = event.value;
  }
}
