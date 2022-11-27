import { Component } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'Network Sniffer Application';
  menuItems: MenuItem[] = [
    {
      label: 'Sniffer',
      icon: 'pi pi-fw pi-home',
      routerLink: ['/sniffer'],
    },
    {
      label: 'Whois',
      icon: 'pi pi-fw pi-user',
      routerLink: ['/whois'],
    },
    {
      label: 'ArpTable',
      icon: 'pi pi-fw pi-table',
      routerLink: ['/arptable'],
    },
  ];

  constructor() {}

  ngOnInit(): void {}
}
