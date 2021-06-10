import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


const headers = new HttpHeaders;
@Injectable({
  providedIn: 'root'
})
export class ServiceService {
  apiUrl = 'http://127.0.0.1:8000/nucleo/api';
  token : any;
  user : any;
  password : any;


  constructor(private http: HttpClient) { }

  login(user:String, password:String) {
    return new Promise((resolve) => {
      this.http
        .post(this.apiUrl + "/token/", {
          user: user,
          password: password,
        })
        .subscribe(
          (data) => {
            this.token = data;
            resolve(data);
            console.log(data);
          },
          (err) => {
            console.log(err);
          }
        );
    });
  }

  getCitas(){
          return new Promise((resolve) => {
        this.http.get(this.apiUrl +"/citas/" ,{
          headers: new HttpHeaders().set('Authorization','token ' + this.token),
        }).subscribe(
          (data) => {
            resolve(data);
          },
          (err) => {
            console.log(err)
          }
        );
      });
    
  }
  
  setToken(valor: any){
    this.token= valor;
  }

  getToken(){
    console.log(this.token);
    return this.token;
  }
}
