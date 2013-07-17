from django.contrib import admin
#from django.contrib.contenttypes import generic
from activa24Duranjo.apps.productos.models import Categoria, CategoriaAdmin, Producto, ImgProductos, ValorDolar

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(ValorDolar)


class ImgProductosInline(admin.TabularInline):
	model = ImgProductos


class ProductoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'codigo', 'descripcion_corta', 'categoria', 'precio_dolares', 'destacado', 'disponible', 'creado_en', 'modificado_en',)
	list_display_links = ('titulo', 'descripcion_corta',)
	list_filter = ('disponible', 'destacado', 'categoria')
	search_fields = ['titulo', 'codigo', 'categoria__titulo', 'precio_dolares']
	inlines = [
		ImgProductosInline,
	]

admin.site.register(Producto, ProductoAdmin)
