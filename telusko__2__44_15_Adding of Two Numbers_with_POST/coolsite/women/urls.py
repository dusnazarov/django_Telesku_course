from django.urls import path
from . import views

urlpatterns=[     
    path('',views.home, name='home'),
    path('addform/',views.addPage, name='addform'),
    path('addform/add',views.add, name='add'),
      
]
