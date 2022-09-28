from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    
    path(r'/', views.home, name='home'),
    path(r'/fileprocess', views.fileprocess, name='fileprocess'),



]
