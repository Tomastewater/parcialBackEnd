from django.contrib import admin
from .models import Examen

@admin.register(Examen)
class adminExamen(admin.ModelAdmin):
    list_display = ["titulo", "fecha", "asignatura", "profesor"]
