import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-arptables',
  templateUrl: './arp-tables.component.html',
  styleUrls: ['./arp-tables.component.css'],
})
export class ArpTablesComponent implements OnInit {
  @Input() text: string = 'NOT SET';
  @Input() color: string = 'black';
  @Output() btnClick = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  onClick() {
    this.btnClick.emit();
  }
}
