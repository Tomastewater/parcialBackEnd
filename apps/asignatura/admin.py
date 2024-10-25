from django.contrib import admin
from .models import Asignatura

@admin.register(Asignatura)
class adminAsignatura(admin.ModelAdmin):
    list_display = ["nombre"]
