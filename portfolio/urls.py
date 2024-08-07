from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('in/<str:uname>/', views.user_profile, name="user_profile"),
    path('login/', views.user_login, name="user_login"),
    path('signin/', views.user_signin, name="user_signin"),
]