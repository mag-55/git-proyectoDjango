from django.urls import path
from . import views
from django.conf import settings #se hacen estas dos importaciones para que aparezcan las imagenes
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name="Servicios"),
]

