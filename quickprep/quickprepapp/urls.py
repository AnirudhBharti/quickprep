from django.conf.urls import url
from .views import GetTutorialMenu, GetTutorialtopicsmenu

urlpatterns =[
url(r'^api/tutorialmenu/', GetTutorialMenu.as_view(), name='tutorial-menu-list'),
url(r'^api/tutorialtopicsmenu/', GetTutorialtopicsmenu.as_view(), name='tutorial-topic-menu-list'),
]