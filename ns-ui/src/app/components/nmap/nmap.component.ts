import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { raw } from 'body-parser';
import { WhoIs } from 'src/app/models/WhoIs';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-nmap',
  templateUrl: './nmap.component.html',
  styleUrls: ['./nmap.component.css'],
})
export class NMapComponent implements OnInit {
  data?: any;

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.nmap().subscribe((data) => {
      this.data = data;
    });
  }
}
