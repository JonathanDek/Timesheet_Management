from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class adminRegistrationForm(UserCreationForm):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()

    class Meta:
        model = User
        fields = ["First_Name","Last_Name","username","Email","password1","password2"]