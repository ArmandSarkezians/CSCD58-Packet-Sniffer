import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ArpTablesComponent } from './components/arptables/arp-tables.component';
import { SnifferComponent } from './components/sniffer/sniffer.component';
import { NMapComponent } from './components/nmap/nmap.component';

const routes: Routes = [
  { path: '', redirectTo: '/sniffer', pathMatch: 'full' },
  { path: 'arptables', component: ArpTablesComponent },
  { path: 'sniffer', component: SnifferComponent },
  { path: 'nmap', component: NMapComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
