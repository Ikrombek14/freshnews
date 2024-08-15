from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.custom_login, name='custom_login'),
    path('password_change/', views.change_password, name='change_password'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
]


