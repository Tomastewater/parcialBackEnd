from django.contrib import admin

from .models import Profesor

@admin.register(Profesor)
class adminProfesor(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "email"]
