from django.contrib import admin
from .models import Event,Fighter,Club,promoters
# Register your models here.
admin.site.register(Event)
admin.site.register(Fighter)
admin.site.register(Club)
admin.site.register(promoters)
