import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ArpTable, ArpTableRow } from 'src/app/models/ArpTable';
import { ApiService } from 'src/app/services/api.service';
import { DialogService } from 'primeng/dynamicdialog';
import { ArpItemComponent } from '../arp-item/arp-item.component';
@Component({
  selector: 'app-arptables',
  templateUrl: './arp-tables.component.html',
  styleUrls: ['./arp-tables.component.css'],
  providers: [DialogService],
})
export class ArpTablesComponent implements OnInit {
  arpTable: ArpTable = [];

  constructor(private api: ApiService, public dialogService: DialogService) {}

  ngOnInit(): void {
    this.api.arpTables().subscribe((data) => {
      this.arpTable = data;
    });
  }

  clickedItem(arp: ArpTableRow) {
    this.api.lookup(arp.ip).subscribe((data) => {
      const ref = this.dialogService.open(ArpItemComponent, {
        data: data,
        header: 'IP Lookup',
        width: '70%',
      });
    });
  }
}
