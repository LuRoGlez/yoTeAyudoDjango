import { Component, OnInit } from '@angular/core';
import { ServiceService } from '../../services/service.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-informes',
  templateUrl: './informes.page.html',
  styleUrls: ['./informes.page.scss'],
})
export class InformesPage implements OnInit {
  mostrar = false;

  constructor(public restService: ServiceService, public router: Router) { }
  citas:any;
  fecha = new Date();



  ngOnInit() {
  }

  mostrarCitas(){
   
    this.getCitas();
    this.mostrar=true;
    
  }

  getCitas(){
    this.restService.getCitas()
       .then((res: any) => {
         if(res){
         this.citas=res;
         console.log(this.citas);
       }
       console.log(res);
      
    },
    
      (error)=>{
        console.error(error);
      }
    );
  }

  irLogin(){
    this.router.navigateByUrl('/login');
  }


}
