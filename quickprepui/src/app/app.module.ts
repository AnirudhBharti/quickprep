import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule,RoutingComponents } from './app-routing.module'
import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { HttpClientModule } from '@angular/common/http';
import { TodoComponent } from './todo/todo.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    RoutingComponents,
    TodoComponent
  ],
  imports: [
    BrowserModule,AppRoutingModule, HttpClientModule
  ],
  providers: [],
  bootstrap: [MenuComponent]
})
export class AppModule { }
