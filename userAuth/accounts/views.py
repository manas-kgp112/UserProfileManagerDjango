from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import * 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import *
from django.contrib.auth.models import User



# Create your views here.

@login_required(login_url='login')
def home(request):
    users = authUser.objects.all()
    context = {'users':users}
    return render(request, 'accounts/home.html', context)



def register(request):
    form = createUserForm()



    if request.method == 'POST':
        form = createUserForm(request.POST)
        if (form.is_valid):
            messages.success(request, 'Account created successfully')
            user = form.save()
            username = form.cleaned_data.get('username')


            authUser.objects.create(
                user = user,
                name = user.username,
            )


            return redirect('login')


    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginFunc(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user')
        else:
            messages.info(request,'Wrong Username or Password')
    context = {}
    return render(request,'accounts/login.html',context)




def  logoutFunc(request):
    logout(request)
    return redirect('login')


def funcUser(request):

    registeredUser = request.user.authuser
    context = {'registeredUser':registeredUser}# ,registeredUser:'registeredUser'}
    return render(request, 'accounts/userProfile.html', context)




def accountSettings(request):
    registeredUser = request.user.authuser
    form = UserForm(instance=registeredUser)
    context = {'registeredUser':registeredUser, 'form':form}

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=registeredUser)
        if form.is_valid():
            form.save()
            return redirect('user')
    return render(request, 'accounts/accountSettings.html', context)