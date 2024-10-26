from django.contrib import admin
from django.urls import path
from apps.examen.views import ExamenView

urlpatterns = [
    path("",ExamenView.as_view(), name="examen"),
    
]