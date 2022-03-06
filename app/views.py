from http.client import ImproperConnectionState
from django.shortcuts import render
import os
from revivalDjango import settings
from .models import Event,Fighter,Club,promoters
import random

# Create your views here.
def home(request):
    eventData = Event.objects.all()
    fighterData = Fighter.objects.all()
    clubData = Club.objects.all()
    promoter = promoters.objects.all()
    all_files = []
    directory_name = os.listdir(os.path.join(settings.BASE_DIR,"static/images"))
    for i in directory_name:
        loop = os.listdir(os.path.join(settings.BASE_DIR,f"static/images/{i}"))
        all_files.append({i:loop})

    return render(request,"index.html",{"events":eventData,"fighter":fighterData,"photos":all_files,"club":clubData,"promoter":promoter})