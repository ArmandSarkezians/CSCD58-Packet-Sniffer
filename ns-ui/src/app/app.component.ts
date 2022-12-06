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
      label: 'nmap',
      icon: 'pi pi-fw pi-user',
      routerLink: ['/nmap'],
    },
    // {
    //   label: 'ArpTable',
    //   icon: 'pi pi-fw pi-table',
    //   routerLink: ['/arptables'],
    // },
    {
      label: 'Network Details',
      icon: 'pi pi-fw pi-table',
      routerLink: ['/arptables'],
    },
  ];

  constructor() {}

  ngOnInit(): void {}
}
