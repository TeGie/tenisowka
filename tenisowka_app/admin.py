from django.contrib import admin
from tenisowka_app.models import *
# Register your models here.

# admin.site.register(Zawodnik, Pojedynek, Wydarzenie)

@admin.register(Player, Match, Event)
class CoachAdmin(admin.ModelAdmin):
    pass