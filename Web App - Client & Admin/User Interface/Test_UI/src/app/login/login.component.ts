import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-login',
    templateUrl:'./login.component.html',
    styleUrls:['./login.component.css']
})

export class LoginComponent implements OnInit{
    title = 'my-app';
    login;
    token = '';
    accountActive:boolean;

    constructor(private userService: UserService, private router: Router) { }

    ngOnInit() {
        this.token = '';
        this.accountActive = true;
        this.login = {
          username: '',
          password: ''
    
        };
    
      }
  
    
    
      loginUser() {
       
        if (this.login.username == 'admin'){
          this.userService.loginUser(this.login).subscribe(
            response => {
              this.token=response["auth_token"]
              localStorage.setItem('auth_tok',this.token)
              console.log(this.token, 'is the auth token')
              this.login = {
                username: '',
                password: ''
                };
                this.router.navigateByUrl("/admin")
            },
            error => console.log('error', error)
          );

        }

       else {

        this.userService.loginUser(this.login).subscribe(
          response => {
            this.token=response["auth_token"]
            localStorage.setItem('auth_tok',this.token)
            console.log(this.token, 'is the auth token')
            this.login = {
              username: '',
              password: ''
              };
              this.router.navigateByUrl("/home")
          },
          error => console.log('error', error)
        ); 
       } 
        
      }

}