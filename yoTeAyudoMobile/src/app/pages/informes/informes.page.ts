import { Component, OnInit } from '@angular/core';
import { ServiceService } from '../../services/service.service';
import { Router } from '@angular/router';
import { getAttrsForDirectiveMatching } from '@angular/compiler/src/render3/view/util';

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
  hoy = this.fecha.getDate();


  ngOnInit() {
  }

  mostrarCitas(){
    console.log(this.hoy);
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
       //console.log(this.citas);
    },
    
      (error)=>{
        console.error(error);
      }
    );
  }


}
