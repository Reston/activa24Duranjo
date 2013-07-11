# coding: utf-8
from django.db import models
from tinymce.models import HTMLField


class Categoria(models.Model):
	titulo = models.CharField(max_length=200)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	imagen = models.ImageField(upload_to='imgcategorias')

	def __unicode__(self):
		return self.titulo


class Producto(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion_corta = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	descripcion = HTMLField()
	categoria = models.ForeignKey(Categoria)
	precio_dolares = models.DecimalField(max_digits=30, decimal_places=3)

	def __unicode__(self):
		return self.titulo


class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')
