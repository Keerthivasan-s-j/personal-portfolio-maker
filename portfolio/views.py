from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

def user_login(request):
    if (request.method == "POST"):
        uname_or_email = request.POST.get("uname_or_email")   
        password = request.POST.get("password")
        error_message = ""
        if ("@" in uname_or_email):
            user = authenticate(email = uname_or_email, password = password)
        else:
            user = authenticate(username = uname_or_email, password = password)
        # the user variable contains the user name of the user if avilable else it contains None
        if user is not None:
            # this login() function is from the contrib.auth whick logins to the user
            login(request, user)
            return redirect(reverse("user_profile", kwargs={"uname" : user})) # keyword argument is used to send data requeired for the url
        else:
            error_message = "Invalid User name or Password"
            return render(request, "auth/login.html", context={"error" : error_message})
    return render(request, "auth/login.html")

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect(reverse("user_login"))

def user_signin(request):
    return render(request, "auth/signin.html")

def home(request):
    if(request.method == "POST"):
        search = request.POST.get("search")
        user = User.objects.filter(username = search)
        if (user is not None):
            return redirect(reverse("user_profile", kwargs={"uname" : search}))
    return render(request, "base/home.html")

def user_profile(request, uname):
    return render(request, "user/profile.html", context={'uname':uname})
# Create your views here.
