from enum import auto
from django.db import models



class Location(models.Model):
    North="North"
    East="East"
    South="South"
    West="West"
    Sector_Choices = [(North,'North'),(East,'East'),(South,'South'), (West,'West')]
    Name = models.CharField(max_length=100)
    Sector = models.CharField(max_length=5, choices=Sector_Choices)

class TimeCard(models.Model):
    North="North"
    East="East"
    South="South"
    West="West"
    Sector_Choices = [(North,'North'),(East,'East'),(South,'South'), (West,'West')]
    Date = models.DateField()
    Sector = models.CharField(max_length=5, choices=Sector_Choices)
    Location = models.CharField(max_length=1000)
    TimeIn = models.TimeField(auto_now = False, auto_now_add = False)
    TimeOut = models.TimeField(auto_now = False, auto_now_add = False)
