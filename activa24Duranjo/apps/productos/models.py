# coding: utf-8
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from decimal import Decimal

class Departamento(models.Model):
	"""docstring for Departamento"""
	titulo = models.CharField(max_length=20, help_text='Hasta 20 caracteres y solamente alfanuméricos', unique=True)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	imagen = models.ImageField(upload_to='imgdepartamentos')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('serviciosyproductos', kwargs={'titulo': titulo})
		
class Categoria(models.Model):
	titulo = models.CharField(max_length=20, help_text='Hasta 20 caracteres y solamente alfanuméricos', unique=True)
	breve_descripcion = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	imagen = models.ImageField(upload_to='imgcategorias')
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('categoria', kwargs={'titulo': titulo})


class Producto(models.Model):
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos')
	codigo = models.CharField(max_length=20)
	descripcion_corta = models.CharField(max_length=140, help_text='Hasta 140 caracteres')
	descripcion = HTMLField()
	categoria = models.ForeignKey(Categoria)
	precio_dolares = models.DecimalField(max_digits=30, decimal_places=2)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
	disponible = models.BooleanField(default=True, help_text='Disponibilidad del producto')
	destacado = models.BooleanField(default=False, help_text='Promocionar producto en sección de destacados')

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('productoproducto', kwargs={'titulo': titulo})


class ImgProductos(models.Model):
	producto = models.ForeignKey(Producto, related_name='imagenes')
	imagen = models.ImageField(upload_to='imgproductos')


class ValorDolar(models.Model):
	dolarEnBolivar = models.DecimalField(max_digits=30, decimal_places=2)

	def __unicode__(self):
		return unicode(self.dolarEnBolivar)

	def get_valor_actual(self, valorEnDolares):
		return (Decimal(valorEnDolares)*Decimal(self.dolarEnBolivar))
