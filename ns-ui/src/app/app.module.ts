import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { MenubarModule } from 'primeng/menubar';
import { TableModule } from 'primeng/table';
import { SelectButtonModule } from 'primeng/selectbutton';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SnifferComponent } from './components/sniffer/sniffer.component';
import { WhoisComponent } from './components/whois/whois.component';
import { ArpTablesComponent } from './components/arptables/arp-tables.component';
import { HeaderComponent } from './components/header/header.component';
import { PacketsComponent } from './components/packets/packets.component';
import { PacketItemComponent } from './components/packet-item/packet-item.component';
import { environment } from 'src/environments/environment';

const config: SocketIoConfig = { url: environment.backendUrl, options: {} };

@NgModule({
  declarations: [
    AppComponent,
    SnifferComponent,
    WhoisComponent,
    ArpTablesComponent,
    HeaderComponent,
    PacketsComponent,
    PacketItemComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SocketIoModule.forRoot(config),
    MenubarModule,
    TableModule,
    SelectButtonModule,
    HttpClientModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
