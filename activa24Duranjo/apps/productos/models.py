# coding: latin-1
from django.db import models

class categoria(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion= models.TextField()
	imagen =  models.ImageField(upload_to='imgcategorias')

class producto(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='imgproductos')
	categoria= models.ForeignKey(categoria)


