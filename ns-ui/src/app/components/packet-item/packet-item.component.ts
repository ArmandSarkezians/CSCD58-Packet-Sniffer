import { Component, OnInit, Input } from '@angular/core';
import { DynamicDialogConfig, DynamicDialogRef } from 'primeng/dynamicdialog';
import { Packet } from '../../models/Packet';

@Component({
  selector: 'app-packet-item',
  templateUrl: './packet-item.component.html',
  styleUrls: ['./packet-item.component.css']
})
export class PacketItemComponent implements OnInit {
  @Input() packet: Packet = {'id': 0};

  constructor(public ref: DynamicDialogRef, public config: DynamicDialogConfig) { }

  ngOnInit(): void {
    this.packet = this.config.data.packet;
    console.log(this.packet);
  }

  toHexString(buffer: any) {
    const byteArray = new Uint8Array(buffer);
    return byteArray.reduce((output, elem) =>
      (output + ('0' + elem.toString(16)).slice(-2)),
      '');
  }

  parseData(arrayBuffer: any) {
    var hex = '';
    var bytes = new Uint8Array(arrayBuffer);

    bytes.forEach((byte) => {
      hex += String.fromCharCode(byte);
    });

    return hex;
  }
}
