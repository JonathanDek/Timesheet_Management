from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    SSN = models.IntegerField()
    Address = models.TextField()
    Phone_Number = models.IntegerField()
    Specialty = models.CharField(max_length = 50)
    Office_Location = models.TextField()

