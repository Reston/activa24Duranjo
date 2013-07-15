from django.conf.urls import patterns, url

urlpatterns = patterns(
	'activa24Duranjo.apps.productos.views',
	url(r'^categoria/(?P<titulo>[-\w]+)/$', 'categoria', name="categoria"),
	url(r'^producto/(?P<titulo>[-\w]+)/$', 'producto', name="productoproducto"),
)
