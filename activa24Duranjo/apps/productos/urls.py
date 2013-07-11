from django.conf.urls import patterns, url

urlpatterns = patterns(
	'activa24Duranjo.apps.productos.views',
	url(r'^(?P<titulo>[-w]+)/$', 'categoria', name="productocategoria"),
	url(r'^producto/$', 'producto', name="productoproducto"),
)
