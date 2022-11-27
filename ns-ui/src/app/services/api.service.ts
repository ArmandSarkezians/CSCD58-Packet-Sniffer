// api service

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { WhoIs } from '../models/WhoIs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}

  whois(): Observable<WhoIs> {
    return this.http.get<WhoIs>(environment.backendUrl + '/whois');
  }
}
