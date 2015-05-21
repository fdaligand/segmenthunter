from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$','stravaOAuth.views.home',name='home'),
    url(r'^authent/$','stravaOAuth.views.authent'),

)
