from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    pass

def registerpage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('homepage')

    return render(request, 'register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def profilepage(request):
    pass

def editprofilepage(request):
    pass

def viewprofilepage(request):
    pass

def dashboardpage(request):
    pass

def resetpasswordpage(request):
    pass

def supportpage(request):
    pass

def settingspage(request):
    pass