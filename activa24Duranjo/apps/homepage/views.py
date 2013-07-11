#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from activa24Duranjo.apps.homepage.forms import *
from django.template import RequestContext
from django.core.mail import send_mail
from activa24Duranjo.apps.productos.models import *


def index(request):
	return render_to_response('homepage/index.html', context_instance=RequestContext(request))


def about(request):
	mision = "misión de la empresa"
	vision = "visión de la empresa"
	ctx = {'mision': mision, 'vision': vision}
	return render_to_response('homepage/sobrenosotros.html', ctx, context_instance=RequestContext(request))


def serviciosyproductos(request):
	categorias= Categoria.objects.all()
	ctx= {'categorias': categorias}
	return render_to_response('homepage/serviciosproductos.html', ctx, context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s RIF: %s Plan: %s' % (cd['nombre'], cd['email'], cd['rif'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@activa24ca.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
