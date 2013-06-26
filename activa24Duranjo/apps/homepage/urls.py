from django.conf.urls import patterns, url

urlpatterns = patterns(
	'duranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^trabajos/$', 'works', name="homepageworks"),
	url(r'^servicios/$', 'services', name="homepageservices"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)
