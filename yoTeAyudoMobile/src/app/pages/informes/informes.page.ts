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

  ngOnInit() {
  }

  mostrarCitas(){
    this.getCitas();
    this.mostrar=true;
    
  }

  getCitas(){
    this.restService.getCitas()
       .then((res: any) => {
         if(res.success){
         this.citas=res.data;
         console.log(this.citas);
       }
    },
    
      (error)=>{
        console.error(error);
      }
    );
  }


}
