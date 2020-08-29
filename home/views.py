from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from .models import Student



def home(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register1.html')


def register1(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        first_yr = request.POST['first_yr']
        last_yr = request.POST['last_yr']
        mobile = request.POST['mobile']
        email = request.POST['email']
        branch = request.POST['branch']
        user_name = request.POST['user_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.create_user(first_name=f_name, last_name=l_name, email=email, password=password,
                                        username=user_name)
        student_user = Student(firstname=f_name, lastname=l_name, email=email, password=password,
                               username=user_name, graduation_starting_year=first_yr, graduation_ending_year=last_yr,
                               mobile_no=mobile, branch=branch)
        user.save()
        student_user.save()
        print("Student Data Added in Database")
        return render(request, 'home/registerfinal.html')
    else:
        return render(request, 'home/studentregister.html')


def register2(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        first_yr = request.POST['first_yr']
        last_yr = request.POST['last_yr']
        mobile = request.POST['mobile']
        email = request.POST['email']
        branch = request.POST['branch']
        user_name = request.POST['user_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.create_user(first_name=f_name, last_name=l_name, email=email, password=password,
                                        username=user_name)
        alumini_user = Student(firstname=f_name, lastname=l_name, email=email, password=password,
                               username=user_name, graduation_starting_year=first_yr, graduation_ending_year=last_yr,
                               mobile_no=mobile, branch=branch)
        user.save()
        alumini_user.save()
        print("Alumini Data Added in Database")
        return render(request, 'home/registerfinal.html')

    else:
        return render(request, 'home/alumniregister.html')


def login_validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('User')
            login(request,user)
            return redirect('home/login.html')
        else:
            print('Not User')
            return redirect('/')
    else:
        return render(request,'home/login.html')
