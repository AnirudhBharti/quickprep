import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MenuList} from '../models/menuModel';
import 'rxjs/Observable';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MenuService {

  public url:string="http://localhost:8000/api/tutorialmenu/";
  constructor(private _http:HttpClient) { 

  }

  getMenu():Observable<MenuList[]>{
    return this._http.get<MenuList[]>(this.url)
  }
}
