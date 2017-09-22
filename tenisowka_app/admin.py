from django.contrib import admin
from tenisowka_app.models import *
# Register your models here.

# admin.site.register(Zawodnik, Pojedynek, Wydarzenie)

@admin.register(Zawodnik, Pojedynek, Wydarzenie)
class TrenerAdmin(admin.ModelAdmin):
    pass