from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register1/', views.register1, name='register1'),
    path('register2/', views.register2, name='register2'),
    path('login/', views.login_validate, name='login'),
    path('logout/', views.logout_validate, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),


]
