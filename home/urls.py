from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register1/', views.register1, name='register1'),
    path('register2/', views.register2, name='register2'),
    path('register3/', views.register3, name='register3'),
    path('login/', views.login, name='login'),


]
