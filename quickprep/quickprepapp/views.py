from django.shortcuts import render
from .models import Tutorialmenu, Tutorialtopics, Tutorialtopicsmenu
from rest_framework import generics, serializers
from rest_framework.views import APIView
from .serializers import TutorialMenuSerializer, TutorialTopicsMenuSerializer
from rest_framework.response import Response
from .mysqldbconnector import gettutorialmenu

# Create your views here.

class GetTutorialMenu(APIView):
     def get(self, request):
     
        tutorialmenus = gettutorialmenu()
              
        tutorialmainmenu =[]
        tutorialsubmenu=[]
     
        for k in tutorialmenus:
            dictionaryMainMenu={}
            dictionarySubMenu={}
            for i, (key,value) in enumerate(k.items()):
                    if(i<=3):
                        dictionaryMainMenu[key]=value
                    else:
                        dictionarySubMenu[key]=value    
            tutorialmainmenu.append(dictionaryMainMenu)
            tutorialsubmenu.append(dictionarySubMenu)
        
        tutorialmainmenu=GetTutorialMenu.removeDuplicates(tutorialmainmenu)
      
        tutorialmenuList = GetTutorialMenu.generateMenu(tutorialmainmenu, tutorialsubmenu)
             
        return Response(tutorialmenuList)

     def generateMenu(tutorialmainmenulist,tutorialsubmenulist):

        newList = []
        itemValue = 0;
        for i, item in enumerate(tutorialmainmenulist):
            itemValue=item['tutorialmenuid']
            item['subMenu']=[]
            
            for j, jitem in enumerate(tutorialsubmenulist):
                if itemValue == jitem['tutorialmenuidfk']:
                    item['subMenu'].append(jitem)
                          
            newList.append(item)

        return newList

     def removeDuplicates(listofElements):
        # Create an empty list to store unique elements
        uniqueList = []
        
        # Iterate over the original list and for each element
        # add it to uniqueList, if its not already there.
        for elem in listofElements:
            if elem not in uniqueList:
                uniqueList.append(elem)
        
        # Return the list of unique elements        
        return uniqueList


class GetTutorialtopicsmenu(APIView):
    def get(self, request):
        tutorialtopicsmenuList = Tutorialtopicsmenu.objects.all()
        #print(tutorialtopicsmenuList.query)
        data = TutorialTopicsMenuSerializer(tutorialtopicsmenuList, many=True).data
        return Response(data)