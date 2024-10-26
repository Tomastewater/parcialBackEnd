from django.urls import path
from apps.asignacionExamen.views import CalificacionesViews, AusentesViews

urlpatterns = [
    path("calificacion/",CalificacionesViews.as_view(), name="examen"),
    path("ausentes/",AusentesViews.as_view(), name="ausente"),
    
]