from re import L
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import adminRegistrationForm

def registar_admin(response):
    if response.method == "POST":
        form = adminRegistrationForm(response.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.is_superuser=1
            admin.save()
        # return redirect("")
    else:
        form = adminRegistrationForm()
    
    return render(response, "registration/registar_admin.html", {"form":form})