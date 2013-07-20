from django.conf.urls import patterns, include, url
from django.conf import settings
from sitemaps import StaticViewSitemap, CategoriaSitemap, ProductoSitemap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
sitemaps = {
	'categoria': CategoriaSitemap,
	'producto': ProductoSitemap,
	'pages': StaticViewSitemap,
}

urlpatterns = patterns(
	'',
	# Examples:
	# url(r'^$', 'activa24Duranjo.views.home', name='home'),
	# url(r'^activa24Duranjo/', include('activa24Duranjo.foo.urls')),
	url(r'^', include('activa24Duranjo.apps.homepage.urls')),
	url(r'^', include('activa24Duranjo.apps.productos.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
