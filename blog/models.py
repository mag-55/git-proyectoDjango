from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    # upload_to hace que las imagenes se carguen con la app blog, 
    # null y blank hace que la imagen sea opcional  
    imagen=models.ImageField(upload_to='blog', null=True, blank=True ) 
    # se usa para eliminar los posts de los usuariso que se eliminen del blog
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    # establecer relacion muchos a muchos 
    categoria=models.ManyToManyField(Categoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo