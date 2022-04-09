from django.conf.urls import url
from django.urls import path
from App_Login import views

urlpatterns = [
    path('Sign_Up/', views.registration, name='Sign_Up'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('Login/', views.User_login, name='Login'),
    path('logout/', views.logoutUser, name='logout')
]
