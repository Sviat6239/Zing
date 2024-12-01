from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    pass

def registerpage(request):
    return render(request, 'register.html')

def loginpage(request):
    return render(request, 'login.html')

def logoutpage(request):
    pass

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