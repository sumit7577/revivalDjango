from django.contrib import admin
from .models import Event,Fighter,Club,Registration,Sponsor,Homebanner
# Register your models here.
admin.site.register(Event)
admin.site.register(Fighter)
admin.site.register(Club)
admin.site.register(Registration)
admin.site.register(Sponsor)
admin.site.register(Homebanner)
