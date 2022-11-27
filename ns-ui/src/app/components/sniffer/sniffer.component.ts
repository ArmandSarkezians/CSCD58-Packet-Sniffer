import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-sniffer',
  templateUrl: './sniffer.component.html',
  styleUrls: ['./sniffer.component.css']
})
export class SnifferComponent implements OnInit {
  @Input() text: string = 'NOT SET';
  @Input() color: string = 'black';
  @Output() btnClick = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  onClick(){
    this.btnClick.emit();
  }

}
