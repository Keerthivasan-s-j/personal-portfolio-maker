from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import *

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
    if request.user.is_authenticated:
        logged_user = get_object_or_404(UserProfile, user=request.user)
    else:
        logged_user = None

    context = {
        'logged_user': logged_user
    }
    if(request.method == "POST"):
        search = request.POST.get("search")
        user = User.objects.filter(username = search).first()
        if (user is not None):
            return redirect(reverse("user_profile", kwargs={"uname" : search}))
    return render(request, "base/home.html", context)

def user_profile(request, uname):
    user = get_object_or_404(User, username=uname)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_about = user_profile.about_me
    user_experience = user_profile.experiences.all()
    user_educations = user_profile.educations.all()
    user_certificates = user_profile.certificates.all()
    user_projects = user_profile.projects.all()
    user_skills = user_profile.skills.all()
    user_languages = user_profile.languages.all()
    if request.user.is_authenticated:
        logged_user = get_object_or_404(UserProfile, user=request.user)
    else:
        logged_user = None

    edit_access = uname == request.user.username

    context = {
        'edit_access': edit_access, 
        'uname': uname, 
        'user_profile': user_profile, 
        'user_about': user_about,
        'user_experience': user_experience,
        'user_educations': user_educations,
        'user_certificates': user_certificates,
        'user_projects': user_projects,
        'user_skills': user_skills,
        'user_languages': user_languages,
        'logged_user': logged_user,
        }

    if request.method == "POST":
        search = request.POST.get("search")
        searched_user = User.objects.filter(username=search).first()

        if searched_user:
            return redirect(reverse("user_profile", kwargs={"uname": search}))
        else:
            return HttpResponse("Profile Not Found!")

    return render(request, "user/profile.html", context)

def personal_details_form(request):
    return render(request, "forms/personal_details_form.html")

@login_required(login_url='user_login')
def del_user_experienc(request,id):
    if request.method == "POST":
        experience = get_object_or_404(Experience, id = id)
        experience.delete()
    return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

@login_required(login_url='user_login')
def del_user_education(request,id):
    if request.method == "POST":
        education = get_object_or_404(Education, id = id)
        education.delete()
    return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

@login_required(login_url='user_login')
def del_user_certificate(request,id):
    if request.method == "POST":
        certificate = get_object_or_404(Certificate, id = id)
        certificate.delete()
    return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

@login_required(login_url='user_login')
def del_user_project(request,id):
    if request.method == "POST":
        project = get_object_or_404(Project, id = id)
        project.delete()
    return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))
# Create your views here.
