from django.views.generic import TemplateView, ListView
from apps.asignacionExamen.models import asignacionExamen

# Create your views here.
    
class CalificacionesViews(TemplateView):
    template_name= "calificaciones.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["asignacionExamen"]= asignacionExamen.objects.all().order_by("calificacion")
        

        return context
    
class AusentesViews(TemplateView):
    template_name= "ausentes.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["asignacionExamen"]= asignacionExamen.objects.all().order_by("alumno").filter(calificacion=None)
        

        return context