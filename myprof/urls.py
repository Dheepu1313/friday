from django.contrib import admin
from django.urls import path, include
from myprof import views

urlpatterns=[
    path('', views.index,name='index'),
    path('home', views.home, name='home'),
     ]