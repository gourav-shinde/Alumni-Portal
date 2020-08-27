from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register1.html')


def register1(request):
    return render(request, 'home/alumniregister.html')


def register2(request):
    return render(request, 'home/studentregister.html')


def register3(request):
    return render(request, 'home/registerfinal.html')


def login(request):
    return render(request, 'home/login.html')
