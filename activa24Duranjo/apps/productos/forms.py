#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms
from tinymce.widgets import TinyMCE

class CategoriaForm(forms.ModelForm):
	titulo = forms.RegexField(regex=r'^[\w ]+$', error_messages={'invalid': ("Caracteres invalidos.")})


class ProductoForm(forms.ModelForm):
	titulo = forms.RegexField(regex=r'^[\w ]+$', error_messages={'invalid': ("Caracteres invalidos.")})
	descripcion = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
