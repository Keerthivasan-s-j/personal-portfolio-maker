from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('in/<str:uname>/', views.user_profile, name="user_profile"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('signin/', views.user_signin, name="user_signin"),
    path('personal_details_form/', views.personal_details_form, name="personal_details_form"),
    path('del_user_experienc/<int:id>', views.del_user_experienc, name="del_user_experienc"),
    path('del_user_education/<int:id>', views.del_user_education, name="del_user_education"),
    path('del_user_certificate/<int:id>', views.del_user_certificate, name="del_user_certificate"),
    path('del_user_project/<int:id>', views.del_user_project, name="del_user_project"),
]