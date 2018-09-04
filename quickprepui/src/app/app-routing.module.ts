import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { DotnetComponent } from './dotnet/dotnet.component';
import { PythonComponent } from './python/python.component';
import { DatastructuresComponent } from './datastructures/datastructures.component';
import { TodoComponent } from './todo/todo.component';

const routes: Routes = [
  {path:'',redirectTo:'/dotnet',pathMatch:'full'},
  {path:'dotnet',component:DotnetComponent},
  {path:'python',component:PythonComponent},
  {path:'datastructures',component:DatastructuresComponent},
  {path:'**',component:TodoComponent},
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const RoutingComponents=[DotnetComponent,
 PythonComponent,DatastructuresComponent,TodoComponent]
