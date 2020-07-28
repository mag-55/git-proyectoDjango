from django.urls import path
from ProyectoWebApp import views
from django.conf import settings #se hacen estas dos importaciones para que aparezcan las imagenes
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.conatcto, name="Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)