from django.contrib import admin
from .models import asignacionExamen

@admin.register(asignacionExamen)
class adminAsignacion(admin.ModelAdmin):
    list_display = ["fechaAsignacion", "fechaResolucion", "calificacion", "observaciones", "examen", "alumno"]
    search_fields = ["examen"]
    list_filter = ["alumno"]
