# -*- encoding: utf-8 -*-
from django.template import Library
from decimal import *
register = Library()


@register.filter
def getimagen(list, mid):
	for i in range(list.count()):
		if list[i].producto_id == mid:
			return list[i].imagen
	return


@register.filter
def getPrecio(valorActual, ValorDolar):
	TWOPLACES = Decimal(10) ** -2
	return (valorActual*ValorDolar).quantize(TWOPLACES)
