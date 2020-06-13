import * as Auth0 from 'auth0-web';
import { CallbackComponent } from './callback.component';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ExamsApiService } from './exams/exams-api.service';

import { ExamFormComponent } from './exams/exam-form.component';
import { RouterModule, Routes } from '@angular/router';
import { ExamsComponent } from './exams/exams.component';

import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule, MatButtonModule, MatCardModule } from '@angular/material';

const appRoutes: Routes = [
  { path: 'callback', component: CallbackComponent },
  { path: 'new-exam', component: ExamFormComponent },
  { path: '', component: ExamsComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    ExamFormComponent,
    ExamsComponent,
    CallbackComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
    ),
    NoopAnimationsModule,
    MatToolbarModule,
    MatButtonModule,
    MatCardModule
  ],
  providers: [ExamsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {
    Auth0.configure({
      domain: 'dev-3-5kafu4.eu.auth0.com',
      audience: 'https://FlaskWithAngular.antra.dk',
      clientID: 'YeoYP75JOKU5g0w73hxecm8pBg4FqBrq',
      redirectUri: 'http://localhost:4200/callback',
      scope: 'openid profile manage:exams'
    });
  }
}