import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule

import { AppComponent } from './app.component';
import { RecipientRegistrationComponent } from './recipient-registration/recipient-registration.component';
import { ReactiveFormsModule } from '@angular/forms';
import { ProviderRegistrationComponent } from './provider-registration/provider-registration.component';
import { MapboxComponent } from './mapbox/mapbox.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { ProviderPostComponent } from './provider-post/provider-post.component';

@NgModule({
  declarations: [
    AppComponent,
    RecipientRegistrationComponent,
    ProviderRegistrationComponent,
    MapboxComponent,
    LoginComponent,
    LogoutComponent,
    ProviderPostComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule, 
    RouterModule.forRoot([]) 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

