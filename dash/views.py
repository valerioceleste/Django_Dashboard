from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'dash/index.html')

def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash:index')
        else:
            messages.error(request, 'Incorrect username or password. Please try again.')

    return render(request, 'dash/login.html')
    
def registration_request(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'dash/signup.html', context)
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        confirmpsw = request.POST['confirmpsw']
        email = request.POST['email']
        
        if password != confirmpsw:
            messages.error(request, 'Passwords do not match. Please enter matching passwords.')
            return render(request, 'dash/signup.html', context)

        try:
            existing_user = User.objects.get(username=username)
            messages.error(request, 'User already exists. Please choose a different username.')
            return render(request, 'dash/signup.html', context)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, 'New user created with success.')
            return redirect("dash:index")
            
