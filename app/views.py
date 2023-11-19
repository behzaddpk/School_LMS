from django.shortcuts import render, redirect, HttpResponse
from .EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser


# Create your views here.
@login_required
def base(request):
    user = CustomUser.objects.get(id = request.user.id)

    context = {
        'user': user
    }
    return render(request, 'base.html', context)

def LOGIN(request):
    return render(request, 'login.html')

def DOLOGIN(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'),)
        if user:
            #user is authenticated
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('HOD')
            elif user_type == '2':
                return redirect('Staff_Home')
            elif user_type == '3':
                return redirect('student_home')         
    else:
        messages.error(request,'Email or Password is incorrect')
        return redirect('login')
    

def LOGOUT(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = CustomUser.objects.get(id = request.user.id)

    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

def UpdateProfile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        profile_pic = request.POST.get('profile_pic')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            
            customuser.first_name = first_name
            customuser.last_name = last_name
            # customuser.profile_pic = profile_pic 
            print(customuser.profile_pic)
            if password !=None and password != "":
                customuser.set_password(password)

            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic=profile_pic
            customuser.save()
            messages.success(request, 'Data updated')
        except:
            messages.error(request, 'Data not updated')

            pass

    return render(request, 'profile.html')