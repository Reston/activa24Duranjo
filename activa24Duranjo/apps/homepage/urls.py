from django.conf.urls import patterns, url

urlpatterns = patterns(
	'activa24Duranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^sobrenosotros/$', 'about', name="homepageabout"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)
