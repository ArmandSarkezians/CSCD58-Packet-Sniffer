import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ArpTablesComponent } from './components/arptables/arp-tables.component';
import { SnifferComponent } from './components/sniffer/sniffer.component';
import { WhoisComponent } from './components/whois/whois.component';

const routes: Routes = [
  { path: '', redirectTo: '/sniffer', pathMatch: 'full' },
  { path: 'arptables', component: ArpTablesComponent },
  { path: 'sniffer', component: SnifferComponent },
  { path: 'whois', component: WhoisComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
