from django.contrib import admin
#from django.contrib.contenttypes import generic
from activa24Duranjo.apps.productos.models import Categoria, Producto, ImgProductos

admin.site.register(Categoria)


class ImgProductosInline(admin.TabularInline):
    model = ImgProductos

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ 
    	ImgProductosInline,
     ]


admin.site.register(Producto, ProductoAdmin)