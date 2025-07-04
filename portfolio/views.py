from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import *
import json

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

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        pronouns = request.POST.get('pronouns')
        dob = request.POST.get('dob')
        district = request.POST.get('location')
        state = '' 
        zip_code = ''

        open_to_work = request.POST.get('status') == 'open'
        profile_picture = request.FILES.get('profile_picture')
        resume = request.FILES.get('resume')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('user_signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        profile = UserProfile.objects.create(
            user=user,
            name=f"{first_name} {last_name}",
            pronouns=pronouns,
            dob=dob,
            district=district,
            state=state,
            zip_code=zip_code,
            open_to_work=bool(open_to_work),
            profile_picture=profile_picture,
            resume=resume
        )

        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('user_profile', uname=user.username)

    return render(request, "auth/signup.html")

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

def about(request):
    logged_user = None
    if request.user.is_authenticated:
        logged_user = UserProfile.objects.get(user=request.user)
        
    if request.method == "POST":
        search = request.POST.get("search")
        searched_user = User.objects.filter(username=search).first()

        if searched_user:
            return redirect(reverse("user_profile", kwargs={"uname": search}))
        else:
            return HttpResponse("Profile Not Found!")
        
    return render(request, 'base/about.html', {
        'logged_user': logged_user,
    })

def user_profile(request, uname):
    user = get_object_or_404(User, username=uname)
    user_profile = get_object_or_404(UserProfile, user=user)
    # user_about = user_profile.about_me
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
        # 'user_about': user_about,
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

def edit_profile_form(request, uname):
    user = get_object_or_404(User, username=uname)
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.user.is_authenticated:
        logged_user = get_object_or_404(UserProfile, user=request.user)
    else:
        logged_user = None

    edit_access = uname == request.user.username
    context = {
        'edit_access': edit_access, 
        'uname': uname, 
        'user_profile': user_profile,
        'logged_user': logged_user,
    }
    return render(request, "forms/edit_profile_form.html", context)

def update_profile(request, uname):
    user = get_object_or_404(User, username=uname)
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.method == "POST":
        fullName = request.POST.get("fullName")
        pronouns = request.POST.get("pronouns")
        dob = request.POST.get("dob")
        location = request.POST.get("location")
        open_to_work = request.POST.get("open_to_work")

        user_profile.name = fullName
        user_profile.pronouns = pronouns
        user_profile.dob = dob
        user_profile.district = location
        user_profile.open_to_work = bool(open_to_work)

        if 'resume' in request.FILES:
            resume_file = request.FILES['resume']
            user_profile.resume = resume_file
            user_profile.save()

        user_profile.save()
    return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

def edit_about_me_form(request, uname):
    user = get_object_or_404(User, username = uname)
    user_profile = get_object_or_404(UserProfile, user = user)
    user_about = user_profile.about_me
    context = {
        'uname' : uname,
        'user_about': user_about,
    }
    return render(request, "forms/edit_about_me_form.html", context)

def update_about(request, uname):
    user = get_object_or_404(User, username = uname)
    user_profile = get_object_or_404(UserProfile, user = user)
    user_about = user_profile.about_me
    if request.method == "POST":
        title = request.POST.get("title")
        about_me = request.POST.get("about_me")

        user_about.title = title
        user_about.about_me = about_me

        user_about.save()
    
    return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

def add_experience(request, uname):
    user = get_object_or_404(User, username = uname)
    user_profile = get_object_or_404(UserProfile, user = user)
    experienc = user_profile.experiences

    context = {
        'uname' : uname,
    }

    if request.method == "POST":
        title = request.POST.get("role")
        company = request.POST.get("company")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        description = request.POST.get("description")

        Experience.objects.create(
            user_profile=user_profile,
            title=title,
            company=company,
            start_date=start_date,
            end_date=end_date,
            description=description
        )

        return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

    return render(request, "forms/add_experience.html", context)

def edit_experience(request, id):
    user = get_object_or_404(User, username = request.user.username)
    experience = get_object_or_404(Experience, id=id)

    context = {
        'experience' : experience,
    }

    if request.method == "POST":
        title = request.POST.get("role")
        company = request.POST.get("company")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        description = request.POST.get("description")

        experience.title = title
        experience.company = company
        experience.description = description
        experience.start_date = start_date
        experience.end_date = end_date

        experience.save()
        return redirect(reverse('user_profile', kwargs={"uname" : request.user.username}))

    return render(request, "forms/edit_experience.html", context)

def edit_education(request, id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    education = get_object_or_404(Education, id=id, user_profile=user_profile)

    if request.method == "POST":
        education.degree = request.POST.get("degree")
        education.school_name = request.POST.get("school_name")
        education.course = request.POST.get("course")
        education.grade = request.POST.get("grade")
        education.start_date = request.POST.get("start_date")
        education.end_date = request.POST.get("end_date") or None  # allow blank

        education.save()
        return redirect(reverse('user_profile', kwargs={"uname": request.user.username}))

    return render(request, "forms/edit_education.html", {'education': education})

def add_education(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    education = user_profile.educations

    if request.method == "POST":
        degree = request.POST.get("degree")
        school_name = request.POST.get("school_name")
        course = request.POST.get("course")
        grade = request.POST.get("grade")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        Education.objects.create(
            user_profile = user_profile,
            degree = degree,
            school_name = school_name,
            course = course,
            grade = grade,
            start_date =start_date,
            end_date = end_date
        )

        
        return redirect(reverse('user_profile', kwargs={"uname": request.user.username}))

    return render(request, "forms/add_education.html", {'education': education})


def edit_certificate(request, id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    certificate = get_object_or_404(Certificate, id=id, user_profile=user_profile)

    if request.method == "POST":
        certificate.title = request.POST.get("title")
        certificate.issued_by = request.POST.get("issued_by")
        certificate.issued_on = request.POST.get("issued_on")
        certificate.certificate_url = request.POST.get("certificate_url")
        certificate.save()

        return redirect(reverse('user_profile', kwargs={"uname": request.user.username}))

    return render(request, "forms/edit_certificate.html", {'certificate': certificate})

def add_certificate(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        issued_by = request.POST.get("issued_by")
        issued_on = request.POST.get("issued_on")
        certificate_url = request.POST.get("certificate_url")

        Certificate.objects.create(
            user_profile=user_profile,
            title=title,
            issued_by=issued_by,
            issued_on=issued_on,
            certificate_url=certificate_url
        )

        return redirect(reverse('user_profile', kwargs={"uname": request.user.username}))

    return render(request, "forms/add_certificate.html")

def edit_project(request, id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    project = get_object_or_404(Project, id=id, user_profile=user_profile)

    if request.method == "POST":
        title = request.POST.get("title")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        description = request.POST.get("description")
        project_url = request.POST.get("project_url")

        project.title = title
        project.start_date = start_date
        project.end_date = end_date
        project.description = description
        project.project_url = project_url
        project.save()

        return redirect(reverse('user_profile', kwargs={'uname': request.user.username}))

    return render(request, "forms/edit_project.html", {"project": project})

def add_project(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        description = request.POST.get("description")
        project_url = request.POST.get("project_url")

        Project.objects.create(
            user_profile=user_profile,
            title=title,
            start_date=start_date,
            end_date=end_date,
            description=description,
            project_url=project_url
        )

        return redirect(reverse('user_profile', kwargs={'uname': request.user.username}))

    return render(request, "forms/add_project.html")

def update_skills(request):
    if request.method == "POST":
        user_profile = request.user.profile
        Skill.objects.filter(user_profile=user_profile).delete()

        skills_json = request.POST.get("skills_data", "[]")
        try:
            skills_list = json.loads(skills_json)
        except json.JSONDecodeError:
            skills_list = []

        for item in skills_list:
            skill_name = item.get("skill", "").strip()
            proficiency = item.get("proficiency", "Beginner").strip()

            if skill_name:
                Skill.objects.create(
                    user_profile=user_profile,
                    skill=skill_name,
                    proficiency=proficiency
                )

        return redirect("user_profile", uname=request.user.username)
    else:
        skills = Skill.objects.filter(user_profile=request.user.profile)
        return render(request, "forms/edit_skills.html", {"skills": skills})

def update_languages(request):
    user_profile = request.user.profile

    if request.method == 'POST':
        raw_data = request.POST.get('languages_data', '[]')
        try:
            data = json.loads(raw_data)
            user_profile.languages.all().delete()
            for lang in data:
                Language.objects.create(
                    user_profile=user_profile,
                    language=lang['language'],
                    proficiency=lang['proficiency']
                )
        except Exception as e:
            print("Invalid JSON:", e)

        return redirect('user_profile', uname=request.user.username)

    return render(request, 'forms/edit_languages.html', {
        'languages': user_profile.languages.all()
    })