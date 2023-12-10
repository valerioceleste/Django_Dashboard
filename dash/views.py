from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import logging

def index(request):
    return render(request, 'dash/index.html')

def user_login(request): #aggiungere warning utoente o password non correta
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash:index')
        else:
            return render(request, 'dash/login.html', context)
    else:
            return render(request, 'dash/login.html', context)
    




def signup(request):
    return render(request, 'dash/signup.html')
