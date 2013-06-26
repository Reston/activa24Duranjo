from django.conf.urls import patterns, include, url
from django.conf import settings
from sitemaps import StaticViewSitemap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
sitemaps = {
	'pages': StaticViewSitemap,
}

urlpatterns = patterns(
	'',
	# Examples:
	# url(r'^$', 'basicoDuranjo.views.home', name='home'),
	# url(r'^basicoDuranjo/', include('basicoDuranjo.foo.urls')),

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
