 export class SubMenuList{
    tutorialtopicsmenuname:string;
    tutorialtopicsmenudescription:string;
    tutorialtopicroute:string;
    tutorialmenuidfk:number
    constructor(){}
}

export class MenuList{
    tutorialmenuid: number;
    tutorialmenuname: string;
    tutorialmenudesc: string;
    tutorialmenuroute:string;
    subMenu:Array<SubMenuList>;
    constructor(){}

}
