from django.conf.urls import patterns, url

urlpatterns = patterns(
	'activa24Duranjo.apps.productos.views',
	url(r'^serviciosyproductos/(?P<titulo>[-\w]+)/$', 'categoria', name="categoria"),
	url(r'^producto/$', 'producto', name="productoproducto"),
)
