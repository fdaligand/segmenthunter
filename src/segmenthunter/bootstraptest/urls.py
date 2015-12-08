from django.conf.urls import patterns,url

urlpatterns = patterns('',

                       url(r'^bootstrap/','bootstraptest.views.test'),
                       )

