from django.conf.urls import patterns, include, url

from ..views import dataApi

urlpatterns = patterns('',
    url(r'^$', dataApi.as_view(), name="home"),

)
