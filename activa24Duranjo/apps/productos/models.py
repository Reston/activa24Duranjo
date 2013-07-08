# coding: latin-1
from django.db import models


class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='imgcategorias')
	def __unicode__(self):
		return self.nombre	


class Producto(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	categoria = models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.nombre	
		
class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')

