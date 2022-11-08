import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Network Sniffer Application';
  showPackets = false;

  constructor() { }

  ngOnInit(): void {}

  toggleSniffer(){
    this.showPackets = !this.showPackets;
  }

  toggleArpTables(){
    console.log('toggle arp tables');
  }

  toggleWhoIs(){
    console.log('toggle whois');
  }

}
