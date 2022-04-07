from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home3(request):
	return render(request, 'Home3.html')

def about():
    ...


def item():
    ...


def login(request):
    if request.user.is_authenticated:
        return redirect('admin')


def logout(request):
    logout(request)
    return redirect('home3')


def admin():
    ...
