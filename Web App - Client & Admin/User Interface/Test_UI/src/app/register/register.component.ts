import { Component, OnInit } from '@angular/core';
import { UserService } from './../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  title = 'my-app';
  register;
  accountActive: boolean;
  errormsg = [];
  msg = [];
  constructor(private userService: UserService, private router: Router) { }

  ngOnInit() {
    this.accountActive = false;
    this.register = {
      email: '',
      username: '',
      password: ''

    };

  }

  reg() {
    return ('Hey')

  }



  registeruser() {
    this.userService.registerUser(this.register).subscribe(
      response => {
        
         
        console.log(this.errormsg)
        alert('User ' + this.register.username + 'has been created')
        this.register = {
          email: '',
          username: '',
          password: ''
         };
         this.router.navigateByUrl("/login")
      },
      error => {
        this.errormsg=error.error.username[0];
          alert(this.errormsg)
         
        

      }

       
    );



  }
  onLogin(event: Event) {
    console.log("this was clicked", event);
    this.accountActive = true;

    this.router.navigate(['/login']);
  }
}
