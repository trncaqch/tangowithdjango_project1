from django.conf.urls import patterns, url
from rango import views
from rango import about


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', about.index ,name='index'))