from dataclasses import fields
from pyexpat import model
from django import forms
from User_Management.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('user','SSN','Address','Phone_Number','Specialty','Office_Location')