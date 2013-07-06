from django.conf.urls import patterns, url

urlpatterns = patterns(
	'activa24Duranjo.apps.productos.views',
	url(r'^categoria/$', 'categoria', name="productocategoria"),
	url(r'^producto/$', 'producto', name="productoproducto"),
)
