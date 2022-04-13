from django.db import models

user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Doctor(models.Model):
    ID = models.ForeignKey(user, on_delete=models.CASCADE)
    SSN = models.IntegerField()
    Address = models.TextField()
    Phone_Number = models.IntegerField()
    Specialty = models.CharField(max_length = 50)
    Office_Location = models.TextField()

