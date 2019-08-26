from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .helpers import check_user_not_exist

#Create your views here.

def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'signUp.html')


def logout_view(request):
    logout(request)
    return redirect(index)


def log_in_page(request):
    return render(request, 'logIn.html')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not check_user_not_exist(email):
            return render(request, 'signUp.html', {'message': 'This email is already token'})

        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name,
                                        last_name=last_name)

        new_user = authenticate(request, username=email, password=password)
        if new_user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(index)


def user_log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(index)
        else:
            if check_user_not_exist(email):
                return render(request, 'logIn.html', {'message': 'Incorrect email'})

            return render(request, 'logIn.html', {'message': 'Incorrect password'})


def user_room(request):
    return render(request, 'cabinet.html')


def user_parameters(request):
    return render(request, 'profile_info.html')