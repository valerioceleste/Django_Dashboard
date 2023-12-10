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
    
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'dash/signup.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        email = request.POST['email']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except User.DoesNotExist:
            logger.debug("{} is a new user".format(username))
        if not user_exist:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect("dash:index")
        else:
            return render(request, 'dash/signup.html', context)

