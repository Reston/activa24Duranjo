#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def producto(request):
	return render_to_response('productos/producto.html', context_instance=RequestContext(request))


def categoria(request):
	return render_to_response('productos/categoria.html', context_instance=RequestContext(request))
