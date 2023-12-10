from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render

def index(request):
    return render(request, 'dash/index.html')

def login(request):
    context = {}
    # Handles POST request
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
    
def logout(request):
    print("Log out the user '{}'".format(request.user.username))
    logout(request)
    return redirect('dash:index')

def signup(request):
    context = {}
    # If it is a GET request, just render the sign up page
    if request.method == 'GET':
        return render(request, 'dash/signup.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to course list page
            login(request, user)
            return redirect("dash:index")
        else:
            return render(request, 'dash/signup.html', context)