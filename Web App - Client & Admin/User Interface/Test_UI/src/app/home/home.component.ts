import { Component, OnInit, Input } from '@angular/core';
import { UserService } from '../user.service';
import { HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
 msg = ''; 
  
  constructor(private userService:UserService) { }

  ngOnInit(): void {
   this.msg = ''; 
   var token = 'Token ' + localStorage.getItem('auth_tok')
 
   this.userService.fetchHomeData(token).subscribe(
     resp=>{
       this.msg=resp
       console.log(this.msg)      

   }) 
  }

}
