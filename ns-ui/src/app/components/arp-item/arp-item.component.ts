import { Component, OnInit, Input } from '@angular/core';
import { DynamicDialogConfig, DynamicDialogRef } from 'primeng/dynamicdialog';
import { ArpData } from 'src/app/models/ArpTable';
import { WhoIs } from 'src/app/models/WhoIs';

@Component({
  selector: 'app-arp-item',
  templateUrl: './arp-item.component.html',
  styleUrls: ['./arp-item.component.css'],
})
export class ArpItemComponent implements OnInit {
  @Input() data: ArpData;

  whois: WhoIs;

  constructor(
    public ref: DynamicDialogRef,
    public config: DynamicDialogConfig
  ) {
    this.config = config;
    this.data = this.config.data;
    this.ref = ref;
    this.whois = this.data?.whois;
  }

  ngOnInit(): void {}
}
