from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Alumni
from django.forms import inlineformset_factory


from .models import *
from .forms import CreateUserForm

def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register1.html')


def register1(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/')

        context = {'form': form}
        return render(request, 'home/studentregister.html', context)


def register2(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/')

        context = {'form': form}
        return render(request, 'home/alumniregister.html', context)


def login_validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('User')
            login(request, user)
            return redirect('/')
        else:
            print('Not User')
            return redirect('home/home1.html')
    else:
        return render(request, 'home/login1.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def contact(request):
    return render(request, 'home/contact.html')


def test(request):
    return render(request, 'home/test.html')
