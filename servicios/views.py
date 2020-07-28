from django.shortcuts import render

from servicios.models import Servicio #importo los servicios guardados en models para motrarlos en la pagina a traves de views

# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})