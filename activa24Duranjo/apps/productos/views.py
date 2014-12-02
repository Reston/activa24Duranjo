#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from activa24Duranjo.apps.productos.models import Departamento, Categoria, Producto, ImgProductos, ValorDolar
from django.shortcuts import get_object_or_404


def producto(request, titulo):
	servicio = False
	titulo = titulo.replace('_', ' ')
	producto = get_object_or_404(Producto, titulo=titulo)
	dolar = ValorDolar.objects.all()[:1]
	imagenes = ImgProductos.objects.filter(producto=producto)
	if (producto.precio_dolares == 0):
		servicio = True
	ctx = {'producto': producto, 'imagenes': imagenes, 'dolar': dolar, 'servicio': servicio}
	return render_to_response('productos/producto.html', ctx, context_instance=RequestContext(request))


def categoria(request, titulo, template='productos/categoria.html', page_template='productos/categoria_productos.html'):
	mensaje = ''
	titulo = titulo.replace('_', ' ')
	categoria = get_object_or_404(Categoria, titulo=titulo)
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
	if request.POST:
		palabra_busqueda = request.POST.get('busqueda', '')
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

def serviciosyproductos(request, titulo, template='productos/serviciosproductos.html', page_template='productos/serviciosproductos_categorias.html'):
	palabra_busqueda = request.POST.get('busqueda', '')
	titulo = titulo.replace('_', ' ')
	mensaje = ''
	departamento = get_object_or_404(Departamento, titulo=titulo)
	categorias = Categoria.objects.filter(departamento=departamento.pk)
	if request.is_ajax():
		template = page_template
	if (palabra_busqueda):
		categorias = Categoria.objects.filter(titulo__icontains=palabra_busqueda)
		if not (categorias):
			mensaje = "No se han encontrado resuldos para "+palabra_busqueda
	ctx = {'departamento': departamento, 'categorias': categorias, 'page_template': page_template, 'mensaje': mensaje}
	return render_to_response(template, ctx, context_instance=RequestContext(request))

def departamento(request):
	departamentos = Departamento.objects.all()
	ctx = {'departamentos': departamentos}
	return render_to_response('productos/departamento.html', ctx, context_instance=RequestContext(request))