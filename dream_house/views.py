from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'signUp.html')


def logout_view(request):
    logout(request)
    return redirect(index)


def log_in_view(request):
    return render(request, 'logIn.html')
