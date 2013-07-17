from django.contrib import admin
#from django.contrib.contenttypes import generic
from activa24Duranjo.apps.productos.models import Categoria, Producto, ImgProductos, ValorDolar
from activa24Duranjo.apps.productos.forms import ProductoForm, CategoriaForm


class CategoriaAdmin(admin.ModelAdmin):
	form = CategoriaForm
	list_display = ('titulo', 'breve_descripcion', 'creado_en', 'modificado_en')
	list_display_links = ('titulo',)
	search_fields = ['titulo', 'breve_descripcion']


class ImgProductosInline(admin.TabularInline):
	model = ImgProductos


class ProductoAdmin(admin.ModelAdmin):
	form = ProductoForm
	list_display = ('titulo', 'codigo', 'descripcion_corta', 'categoria', 'precio_dolares', 'destacado', 'disponible', 'creado_en', 'modificado_en',)
	list_display_links = ('titulo', 'descripcion_corta',)
	list_filter = ('disponible', 'destacado', 'categoria')
	search_fields = ['titulo', 'codigo', 'categoria__titulo', 'precio_dolares']
	inlines = [
		ImgProductosInline,
	]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ValorDolar)
