import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule  } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';

import { ComponentsComponent } from './components/components.component';
import { ProfileComponent } from './examples/profile/profile.component';
import { SignupComponent } from './examples/signup/signup.component';
import { LandingComponent } from './examples/landing/landing.component';
import { NucleoiconsComponent } from './components/nucleoicons/nucleoicons.component';
import { LoginComponent } from './examples/login/login.component';
import { HomeComponent } from './examples/home/home.component';

const routes: Routes =[
    { path: '', redirectTo: 'landing', pathMatch: 'full' },
    { path: 'end',              component: ComponentsComponent },
    { path: 'home',             component: HomeComponent},
    { path: 'admin',            component: ProfileComponent },
    { path: 'signup',           component: SignupComponent },
    { path: 'login',            component: LoginComponent },
    { path: 'landing',          component: LandingComponent },
    { path: 'nucleoicons',      component: NucleoiconsComponent }
];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes,{useHash: true})
  ],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule { }
