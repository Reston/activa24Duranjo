#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from activa24Duranjo.apps.productos.models import Categoria, Producto, ImgProductos


def producto(request):
	return render_to_response('productos/producto.html', context_instance=RequestContext(request))


def categoria(request, template='productos/categoria.html', page_template='productos/categoria_productos.html', titulo=None):
	titulo = titulo.replace('_', ' ')
	categoria = Categoria.objects.get(titulo=titulo)
	lista_categorias = Categoria.objects.all()
	productos = Producto.objects.filter(categoria=categoria.pk)
	imagenes = ImgProductos.objects.filter(producto__in=productos)
	if request.is_ajax():
		template = page_template
	ctx = {'categoria': categoria, 'page_template': page_template, 'productos': productos, 'imagenes': imagenes, 'lista_categorias': lista_categorias}
	return render_to_response(template, ctx, context_instance=RequestContext(request))
