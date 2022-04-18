from enum import auto
from django.db import models

Sector_Choices = [(1,'North'),(2,'East'),(3,'South'), (4,'West')]

class Location(models.Model):
    Name = models.CharField(max_length=100)
    Sector = models.IntegerField(choices=Sector_Choices)

class TimeCard(models.Model):
    Date = models.DateField()
    location = models.ForeignKey(Location, blank="Fale", null="False", on_delete=models.CASCADE)
    TimeIn = models.TimeField(auto_now = False, auto_now_add = False)
    TimeOut = models.TimeField(auto_now = False, auto_now_add = False)
    Hours = models.IntegerField()