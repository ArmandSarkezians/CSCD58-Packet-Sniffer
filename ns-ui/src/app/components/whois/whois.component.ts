import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { raw } from 'body-parser';
import { WhoIs } from 'src/app/models/WhoIs';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-whois',
  templateUrl: './whois.component.html',
  styleUrls: ['./whois.component.css'],
})
export class WhoisComponent implements OnInit {
  data?: WhoIs;
  raw?: string;

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.whois().subscribe((data) => {
      let { raw, ...whois } = data;
      this.data = whois as WhoIs;
      this.raw = raw;
    });
  }
}
