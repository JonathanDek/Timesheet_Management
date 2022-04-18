from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import logging

def login(request):
    logging.basicConfig(level=logging.NOTSET)
    if request.method == 'POST':
        data=request.POST
        form = AuthenticationForm(data)
        if form.is_valid:
            user_name = request.POST.get('username', None)
            user_obj = User.objects.get(username = user_name)
            if user_obj.is_superuser:
                logging.info("Hello there")
                return render(request, "User_Management/admin_site.html", {})
            else:
                return render(request, "User_Management/doctor_site.html", {})
    else:
        logging.info("Didn't make it")
        form = AuthenticationForm()
    return render(request,'User_Management/login.html',{'form':form})

def user_list(request):
    return render(request, "User_Management/user_list.html", {})

def create_user(request):
    return render(request, "User_Management/create_user.html", {})

def edit_user(request):
    return render(request, "User_Management/edit_user.html", {})

def base(request):
    return render(request, "User_Management/base.html", {})

def doctor_site(request):
    return render(request, "User_Management/doctor_site.html", {})

def admin_site(request):
    return render(request, "User_Management/admin_site.html", {})