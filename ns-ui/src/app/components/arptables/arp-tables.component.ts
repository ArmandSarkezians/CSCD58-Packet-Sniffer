import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ArpTable } from 'src/app/models/ArpTable';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-arptables',
  templateUrl: './arp-tables.component.html',
  styleUrls: ['./arp-tables.component.css'],
})
export class ArpTablesComponent implements OnInit {
  arpTable: ArpTable = [];

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.arpTables().subscribe((data) => {
      this.arpTable = data;
    });
  }
}
