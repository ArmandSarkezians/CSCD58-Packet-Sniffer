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
}
