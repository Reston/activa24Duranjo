#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from activa24Duranjo.apps.productos.models import Categoria, Producto


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 1
	changefreq = 'yearly'

	def items(self):
		return [
				'homepageindex',
				"homepageabout",
				"departamento",
				"homapagecontact",
				]

	def location(self, item):
		return reverse(item)


class CategoriaSitemap(sitemaps.Sitemap):
	changefreq = 'monthly'
	priority = 0.5

	def items(self):
		return Categoria.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en


class ProductoSitemap(sitemaps.Sitemap):
	changefreq = 'weekly'
	priority = 0.6

	def items(self):
		return Producto.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en
