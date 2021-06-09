import { Component, OnInit } from '@angular/core';
import { ServiceService } from '../../services/service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  user: any;
  password: any;
  token: any;

  constructor(public restService: ServiceService, public router: Router) { }

  ngOnInit() {
  }

  login(){
    this.restService.login(this.user, this.password).then(data=>{
      console.log(data);
      this.token = data;
      this.restService.setToken(this.token.data.token);
      if(this.token.success){
        console.log('Login correcto');
       
          this.router.navigateByUrl('/informes');
        
       }
    });
    
  }

}
