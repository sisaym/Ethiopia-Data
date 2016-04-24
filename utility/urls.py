from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = patterns('',
      # url(r'^$', views.HomePageList.as_view(), name="home"),
      url(r'^$', views.return_home_pages_list.as_view(), name="home"),
)
