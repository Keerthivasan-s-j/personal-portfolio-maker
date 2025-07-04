from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name="home"),

    # Nav Links
    path('about/', views.about, name="about"),

    # Authentication
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('signup/', views.user_signup, name="user_signup"),

    # Profile View & Edit
    path('in/<str:uname>/', views.user_profile, name="user_profile"),
    path('edit_profile_form/<str:uname>/', views.edit_profile_form, name="edit_profile_form"),
    path('update_profile/<str:uname>/', views.update_profile, name="update_profile"),
    path('personal_details_form/', views.personal_details_form, name="personal_details_form"),

    # About Section
    path('edit_about_me_form/<str:uname>/', views.edit_about_me_form, name="edit_about_me_form"),
    path('update_about/<str:uname>/', views.update_about, name="update_about"),

    # Experience
    path('add_experience/<str:uname>/', views.add_experience, name="add_experience"),
    path('edit_experience/<int:id>/', views.edit_experience, name="edit_experience"),
    path('del_user_experienc/<int:id>/', views.del_user_experienc, name="del_user_experienc"),

    # Education
    path('add_education/', views.add_education, name="add_education"),
    path('edit_education/<int:id>/', views.edit_education, name="edit_education"),
    path('del_user_education/<int:id>/', views.del_user_education, name="del_user_education"),

    # Certificates & Projects
    path('add_certificate/', views.add_certificate, name='add_certificate'),
    path('edit_certificate/<int:id>/', views.edit_certificate, name="edit_certificate"),
    path('del_user_certificate/<int:id>/', views.del_user_certificate, name="del_user_certificate"),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:id>/', views.edit_project, name='edit_project'),
    path('del_user_project/<int:id>/', views.del_user_project, name="del_user_project"),

    # Skills
    path('update_skills/', views.update_skills, name='update_skills'),
    
    # Languages Known
    path('update_languages/', views.update_languages, name='update_languages'),

]
