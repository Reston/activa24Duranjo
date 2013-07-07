# coding: latin-1
from django.db import models


class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='imgcategorias')


class Producto(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='imgproductos')
	categoria = models.ForeignKey(Categoria)
