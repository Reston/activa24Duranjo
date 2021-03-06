#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from activa24Duranjo.apps.homepage.forms import *
from django.template import RequestContext
from django.core.mail import send_mail
from activa24Duranjo.apps.productos.models import *
from activa24Duranjo.apps.slider.models import SliderItem
from zinnia.models import Entry
import nltk


def index(request):
	slideritem = SliderItem.objects.all()
	productos = Producto.objects.all().order_by('creado_en')[:3]
	imagenes = ImgProductos.objects.filter(producto__in=list(productos))
	#entradas de blog
	entradas = Entry.objects.order_by('-creation_date')[:3]
	for ent in entradas:
		quitar_html= nltk.clean_html(ent.content) 
		ent.content =  quitar_html[:65]
	ctx = {'slideritem': slideritem, 'productos': productos, 'imagenes': imagenes, 'entradas': entradas}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
	mision = "misión de la empresa"
	vision = "visión de la empresa"
	ctx = {'mision': mision, 'vision': vision}
	return render_to_response('homepage/sobrenosotros.html', ctx, context_instance=RequestContext(request))

def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s RIF: %s ' % (cd['nombre'], cd['email'], cd['rif'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, 'contacto@activa24ca.com', ['contacto@activa24ca.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
