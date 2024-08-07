from django.shortcuts import render

def user_login(request):
    return render(request, "auth/login.html")

def user_signin(request):
    return render(request, "auth/signin.html")

def home(request):
    return render(request, "base/home.html")

def user_profile(request, uname):
    return render(request, "user/profile.html", context={'uname':uname})
# Create your views here.
