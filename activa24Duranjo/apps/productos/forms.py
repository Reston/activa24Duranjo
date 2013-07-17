#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms


class CategoriaForm(forms.ModelForm):
	titulo = forms.RegexField(regex=r'^[\w ]+$', error_messages={'invalid': ("Caracteres invalidos.")})


class ProductoForm(forms.ModelForm):
	titulo = forms.RegexField(regex=r'^[\w ]+$', error_messages={'invalid': ("Caracteres invalidos.")})
