import { Component, OnInit } from '@angular/core';
import { MenuService } from '../menu.service'
import {MenuList } from '../../models/menuModel'

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  
  public MenuList: MenuList[]
  constructor(private menuService: MenuService) { }

  ngOnInit() {
    this.menuService.getMenu().subscribe(data => {
        this.MenuList = data
        console.log(this.MenuList)
    });

  }

}
