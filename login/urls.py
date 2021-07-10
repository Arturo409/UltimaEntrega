from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, HttpResponse




urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('login/', views.loginPage, name="login"),
    path('registro', views.registro, name='registro'),
    path('logout', views.logoutUser, name='logout'),
]