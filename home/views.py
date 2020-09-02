from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user
from .forms import CreateUserForm

def home(request):
    return render(request, 'home/home.html')

@unauthenticated_user
def register(request):
    return render(request, 'home/register1.html')

# social authentication setting
@unauthenticated_user
def register1(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')

    context = {'form': form}
    return render(request, 'home/studentregister.html', context)

@unauthenticated_user
def register2(request):
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

@unauthenticated_user
def login_validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('User')
            login(request, user)
            user = User.objects.get(username=username)
            return redirect('/')
        else:
            print('Not User')
            messages.info(request,"Username or Password incorrect !")
            return render(request, 'home/login.html',)
    else:
        return render(request, 'home/login.html')


def logout_validate(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login')
def contact(request):
    return render(request, 'home/contact.html')


def test(request):
    return render(request, 'home/test.html')


@login_required(login_url='/login')
def profile(request):
    return render(request, 'home/profile_page.html')


