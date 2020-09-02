from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import CreateUserForm

def home(request):
    return render(request, 'home/home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'home/register1.html')

# social authentication setting
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/home.html"


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
                return redirect('/login')

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
    if request.user.is_authenticated:
        return redirect('/')
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
            messages.info(request,"Username or Password incorrect !")
            return render(request, 'home/login.html',)
    else:
        return render(request, 'home/login.html')


def logout_validate(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login')
def contact(request):
    return render(request, 'home/login.html')


def test(request):
    return render(request, 'home/test.html')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'home/profile_page.html')


