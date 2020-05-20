from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path(route='admin',view= views.admin,kwargs=None,name='admin')
]