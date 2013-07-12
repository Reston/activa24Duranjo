from django.conf.urls import patterns, url
from activa24Duranjo.apps.productos.views import categoria

urlpatterns = patterns(
	'activa24Duranjo.apps.productos.views',
	url(r'^serviciosyproductos/(?P<titulo>[-\w]+)/$', 'categoria', name="categoria"),
	url(r'^producto/$', 'producto', name="productoproducto"),
)
