from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('in/<str:uname>/', views.user_profile, name="user_profile"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('signin/', views.user_signin, name="user_signin"),
    path('personal_details_form/', views.personal_details_form, name="personal_details_form"),
]