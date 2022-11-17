import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-arptables',
  templateUrl: './arptables.component.html',
  styleUrls: ['./arptables.component.css']
})
export class ArptablesComponent implements OnInit {
  @Input() text: string = 'NOT SET';
  @Input() color: string = 'black';
  @Output() btnClick = new EventEmitter();

  constructor() {}

  ngOnInit(): void {}

  onClick(){
    this.btnClick.emit();
  }
}
