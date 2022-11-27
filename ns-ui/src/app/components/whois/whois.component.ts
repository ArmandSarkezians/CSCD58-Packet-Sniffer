import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-whois',
  templateUrl: './whois.component.html',
  styleUrls: ['./whois.component.css']
})
export class WhoisComponent implements OnInit {
  @Input() text: string = 'NOT SET';
  @Input() color: string = 'black';
  @Output() btnClick = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  onClick(){
    this.btnClick.emit();
  }
}
