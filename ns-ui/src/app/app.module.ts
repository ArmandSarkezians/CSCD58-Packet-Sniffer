import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SnifferComponent } from './components/sniffer/sniffer.component';
import { WhoisComponent } from './components/whois/whois.component';
import { ArptablesComponent } from './components/arptables/arptables.component';
import { HeaderComponent } from './components/header/header.component';
import { PacketsComponent } from './components/packets/packets.component';
import { PacketItemComponent } from './components/packet-item/packet-item.component';

const config: SocketIoConfig = { url: 'http://localhost:5000', options: {} };

@NgModule({
  declarations: [
    AppComponent,
    SnifferComponent,
    WhoisComponent,
    ArptablesComponent,
    HeaderComponent,
    PacketsComponent,
    PacketItemComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, SocketIoModule.forRoot(config)],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}