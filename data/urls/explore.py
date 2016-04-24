from django.conf.urls import patterns, url

from ..views import ExploreView

urlpatterns = patterns('',
    url(r'^$', ExploreView.as_view(), name="home"),

)
