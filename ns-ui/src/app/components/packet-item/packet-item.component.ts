import { Component, OnInit, Input } from '@angular/core';
import { Packet } from '../../models/Packet';

@Component({
  selector: 'app-packet-item',
  templateUrl: './packet-item.component.html',
  styleUrls: ['./packet-item.component.css']
})
export class PacketItemComponent implements OnInit {
  @Input() packet: Packet = {'id': 0};

  constructor() { }

  ngOnInit(): void {
  }

}
