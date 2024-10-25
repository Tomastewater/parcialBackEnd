from django.views.generic import TemplateView, ListView
from apps.examen.models import Examen


# Create your views here.

class ExamenView(TemplateView):
    template_name= "examenesCreados.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["examen"]= Examen.objects.all().order_by("titulo")
        

        return context
    
