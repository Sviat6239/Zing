import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

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
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('login')


@login_required
def editprofilepage(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                avatar = form.cleaned_data.get('avatar')
                if avatar:
                    random_string = get_random_string(length=8)
                    extension = avatar.name.split('.')[-1]
                    avatar.name = f"profile_{random_string}.{extension}"
                    user.avatar = avatar
                form.save()
                return redirect('profile')
        else:
            form = UserProfileForm(instance=user)

        return render(request, 'editprofile.html', {'form': form})
    else:
        return redirect('login')

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