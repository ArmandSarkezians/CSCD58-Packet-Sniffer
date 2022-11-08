import { Component, OnInit } from '@angular/core';
import { PACKETS } from '../../mockpackets';
import { Packet } from '../../Packet';


@Component({
  selector: 'app-packets',
  templateUrl: './packets.component.html',
  styleUrls: ['./packets.component.css']
})
export class PacketsComponent implements OnInit {
  packets = PACKETS;

  constructor() { }

  ngOnInit(): void {
  }

}
