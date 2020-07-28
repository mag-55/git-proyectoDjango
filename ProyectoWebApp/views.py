from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")
    #return HttpResponse("Home")

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")
    
def conatcto(request):
    return render(request, "ProyectoWebApp/contacto.html")