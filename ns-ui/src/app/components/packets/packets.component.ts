import { Component, OnInit, OnDestroy } from '@angular/core';
import { PACKETS } from '../../samples/mockpackets';
import { Packet, PacketTable } from '../../models/Packet';
import { Socket } from 'ngx-socket-io';
import { DialogService } from 'primeng/dynamicdialog';
import { PacketItemComponent } from '../packet-item/packet-item.component';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-packets',
  templateUrl: './packets.component.html',
  styleUrls: ['./packets.component.css'],
  providers: [DialogService],
})
export class PacketsComponent implements OnInit, OnDestroy {
  packets = [] as PacketTable[];
  messages: any[] = [];

  MAX_PACKETS = 300;

  update = false;
  options = [
    { l: 'On', v: true },
    { l: 'Off', v: false },
  ];

  constructor(
    private api: ApiService,
    private socket: Socket,
    public dialogService: DialogService
  ) {}

  ngOnInit(): void {
    this.subscribeToSocket();
    window.onbeforeunload = (e) => {
      this.update = false;
      this.socket.disconnect();
      this.socket.removeAllListeners();
    };
  }

  ngOnDestroy(): void {
    this.update = false;
    this.socket.disconnect();
    this.socket.removeAllListeners();
  }

  subscribeToSocket() {
    this.socket.fromEvent('packets').subscribe((data: any) => {
      this.packets.unshift(data);

      if (this.packets.length > this.MAX_PACKETS) {
        // remove 100 packets
        this.packets.splice(this.MAX_PACKETS - 100, 100);
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

  toHexString(buffer: any) {
    const byteArray = new Uint8Array(buffer);
    return byteArray.reduce(
      (output, elem) => output + ('0' + elem.toString(16)).slice(-2),
      ''
    );
  }

  parseData(arrayBuffer: any) {
    var hex = '';
    var bytes = new Uint8Array(arrayBuffer);

    bytes.forEach((byte) => {
      hex += String.fromCharCode(byte);
    });

    return hex;
  }

  toggleUpdating(event: any) {
    this.update = event.value;

    if (!this.update) {
      this.socket.disconnect();
    } else {
      this.socket.connect();
      this.api.startSniffing().subscribe((data) => {
        console.log(data);
      });
    }
  }
}
