import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { AdminComponent } from './admin/admin.component';

const routes: Routes =[
    {path: '', component:RegisterComponent},
    { path : 'login', component: LoginComponent},
    { path : 'register', component: RegisterComponent},
    { path : 'home', component: HomeComponent},
    { path : 'admin', component: AdminComponent}

]

@NgModule({
    imports: [
        RouterModule.forRoot(routes,{useHash:true,enableTracing:false})
    ],
    exports: [RouterModule],
    declarations: []
})
export class AppRoutingModule{}
