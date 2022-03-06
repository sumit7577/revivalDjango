
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


class promoters(models.Model):
    image = models.ImageField(upload_to="sponsor",blank=False)
    name = models.CharField(max_length=30,default="",unique=True,blank=False)

    def __str__(self) -> str:
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30,default="",unique=True,blank=False)
    image = models.ImageField(upload_to="clubs",blank=True)
    location = models.CharField(max_length=120,default="",unique=False,blank=False)

    def __str__(self) -> str:
        return self.name