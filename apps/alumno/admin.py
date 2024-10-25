from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class adminAlumno(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "email", "numeroIdentificador"]

    
