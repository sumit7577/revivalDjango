from django.shortcuts import redirect, render
import os
from revivalDjango import settings
from .models import Event,Fighter,Club,Registration,Sponsor,Homebanner
from django.core.mail import send_mail

# Create your views here.
host_email = "contact@bilsha.co.uk"
host_password = "Twins2010"
def home(request):
    #send_mail('test','some message',host_email,['asmitkumarr082@gmail.com'],fail_silently=False,auth_user=host_email,auth_password=host_password)
    eventData = Event.objects.all()
    fighterData = Fighter.objects.all()
    clubData = Club.objects.all()
    sponsorData = Sponsor.objects.all()
    bannerData = Homebanner.objects.all()
    all_files = []
    directory_name = os.listdir(os.path.join(settings.BASE_DIR,"static/images"))
    for i in directory_name:
        loop = os.listdir(os.path.join(settings.BASE_DIR,f"static/images/{i}"))
        all_files.append({i:loop})

    return render(request,"index.html",{"events":eventData,"fighter":fighterData,"photos":all_files,"club":clubData,"sponsor":sponsorData,"homebanner":bannerData})

def register(request):
    if request.method == "POST":
        name = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        date = request.POST.get("dob")
        age = request.POST.get("age")
        number = request.POST.get("number")
        email = request.POST.get("email")
        coach = request.POST.get("coach")
        gym= request.POST.get("gym")
        frequency = request.POST.get("frequency")
        exp = request.POST.get("experience")
        uniqueId= request.headers.get("Cookie").split(';')[0]
        try:
            validation= Registration.objects.get(email=email)
            if validation is not None:
                return render(request,"register.html",{"message":"Email is already registered!"})
        except:
            pass
        
        try:
            validation2 = Registration.objects.get(uniqueId=uniqueId)
            if validation2 is not None:
                return redirect("/")
        except:
            pass
    
        try:
            Registration.objects.create(firstname=name,lastname=lastname,height=height,weight=weight,date=date,age=age,number=number,email=email,coach=coach,
            gym=gym,frequency=frequency,experience=exp,uniqueId=uniqueId)
            return render(request,"register.html",{"message":"Registration Successfull!","success":True})
        except Exception as E:
            return render(request,"register.html",{"message":"Please fill all form correctly"})
        

    return render(request,"register.html")