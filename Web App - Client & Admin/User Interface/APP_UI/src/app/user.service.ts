import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs'
const headers =new HttpHeaders();

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

registerUser(userData): Observable<any> {
  return this.http.post('http://127.0.0.1:8000/auth/users/', userData);
}
loginUser(userData): Observable<any> {
  return this.http.post('http://127.0.0.1:8000/auth/token/login', userData);
}
fetchHomeData(token):Observable<any> {
  return this.http.get('http://127.0.0.1:8000/auth/restricted/',{headers: new HttpHeaders().set('Authorization',token)} );
} 
}
