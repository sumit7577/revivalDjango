from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30,default="",unique=True,blank=False)
    description = models.CharField(max_length=120,default="",unique=False,blank=False)
    location = models.CharField(max_length=30,default="",unique=False,blank=False)
    time = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to = "events",blank=False)

    def __str__(self) -> str:
        return self.title


class Fighter(models.Model):
    name = models.CharField(max_length=30,default="",unique=True,blank=False)
    fights = models.IntegerField(default=1,blank=False)
    win = models.IntegerField(default=0,blank=False,unique=False)
    Loss = models.IntegerField(default=0,blank=False,unique=False)
    club = models.CharField(max_length=50,default="",unique=False,blank=False)
    ranking = models.IntegerField(default=1,blank=False,unique=False)
    image = models.ImageField(upload_to="fighters",blank=True)


    def __str__(self) -> str:
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30,default="",unique=True,blank=False)
    image = models.ImageField(upload_to="clubs",blank=True)
    location = models.CharField(max_length=120,default="",unique=False,blank=False)

    def __str__(self) -> str:
        return self.name

class Registration(models.Model):
    firstname = models.CharField(max_length=30,default="",unique=False,blank=False)
    lastname = models.CharField(max_length=30,default="",unique=False,blank=False)
    height = models.IntegerField(default=0,unique=False,blank=False)
    weight = models.IntegerField(default=0,unique=False,blank=False)
    date = models.DateField(default=timezone.now(),blank=False)
    age = models.IntegerField(default=0,unique=False,blank=False)
    number = models.IntegerField(default=0,unique=False,blank=False)
    email = models.CharField(max_length=40,default="",unique=True,blank=False)
    coach = models.CharField(max_length=40,default="",unique=False,blank=False)
    gym = models.CharField(max_length=40,default="",unique=False,blank=False)
    frequency = models.IntegerField(default=0,unique=False,blank=False)
    experience = models.IntegerField(default=0,unique=False,blank=False)
    uniqueId = models.CharField(blank=False,unique=True,max_length=200)


    def __str__(self) -> str:
        return self.firstname

class Sponsor(models.Model):
    title = models.CharField(max_length=30,default="",blank=True,unique=True)
    filename = models.ImageField(blank=False,upload_to="sponsor")

    def __str__(self) -> str:
        return self.title

class Homebanner(models.Model):
    title = models.CharField(max_length=30,default="",blank=True,unique=True)
    filename = models.ImageField(blank=False,upload_to="sponsor")

    def __str__(self) -> str:
        return self.title