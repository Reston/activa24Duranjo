#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from activa24Duranjo.apps.productos.models import Categoria, Producto, ImgProductos, ValorDolar


def producto(request, titulo):
	servicio= False
	titulo = titulo.replace('_', ' ')
	producto = Producto.objects.get(titulo=titulo)
	dolar = ValorDolar.objects.all()[:1]
	imagenes = ImgProductos.objects.filter(producto=producto)
	if (producto.precio_dolares == 0):
		servicio= True
	ctx = {'producto': producto, 'imagenes': imagenes, 'dolar': dolar, 'servicio':servicio}
	return render_to_response('productos/producto.html', ctx, context_instance=RequestContext(request))


def categoria(request, template='productos/categoria.html', page_template='productos/categoria_productos.html', titulo=None):
	palabra_busqueda = request.POST.get('busqueda', '')
	mensaje = ''
	titulo = titulo.replace('_', ' ')
	categoria = Categoria.objects.get(titulo=titulo)
	lista_categorias = Categoria.objects.all()
	productos = Producto.objects.filter(categoria=categoria.pk)
	destacados = productos.filter(destacado=True)[:2]
	if destacados:
		dolar = ValorDolar.objects.all()[:1]
	else:
		dolar = None
	imagenes = ImgProductos.objects.filter(producto__in=productos)
	if request.is_ajax():
		template = page_template
	if (palabra_busqueda):
		productos = Producto.objects.filter(titulo__icontains=palabra_busqueda)
		if not (productos):
			mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {
		'categoria': categoria,
		'page_template': page_template,
		'productos': productos,
		'destacados': destacados,
		'dolar': dolar,
		'imagenes': imagenes,
		'lista_categorias': lista_categorias,
		'mensaje': mensaje
	}
	return render_to_response(template, ctx, context_instance=RequestContext(request))
