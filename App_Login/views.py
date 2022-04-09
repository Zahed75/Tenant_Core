from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from App_Login.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import redirect


# Create your views here.


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/Sign_Up/')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/Sign_Up/')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            profile_obj = Profile.objects.create(user=user_obj)
            profile_obj.save()
            return redirect('/Login/')

        except Exception as e:
            print(e)
    dict = {}

    return render(request, 'App_Login/Register.html', context=dict)


def user_profile(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        nid = request.POST.get('nid')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')

        setup_profile = UserProfile(
            full_name=full_name,
            nid=nid,
            phone_number=phone_number,
            gender=gender,
            user=request.user
        )
        setup_profile.save()
        return redirect('/tenant_dashboard/')

    dict = {}

    return render(request, 'App_Login/User_Profile.html', context=dict)


def User_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/Login/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/Login/')

        login(request, user)
        
        if UserProfile.objects.filter(user=user_obj):
            return redirect('/tenant_dashboard/')
        else:
            return redirect('/user_profile')

    dict = {}

    return render(request, 'App_Login/login.html', context=dict)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('Login')
