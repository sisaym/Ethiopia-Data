from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import View


from data.urls import urls as data_urls
from utility.views import return_home_pages_list, ApiPage
from publications import urls as publications_urls
from data.urls import export as export_urls
from data.urls import agriculture as agriculture_urls
from data.urls import import_urls as import_urls
from data.urls import explore as explore_urls
from data import api

urlpatterns = patterns('',
    # Examples:
    url(r'^$', return_home_pages_list.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/agriculture/',include(agriculture_urls, namespace='data_agriculture')),
    url(r'^data/imports/', include(import_urls, namespace="data_imports")),
    url(r'^data/exports/', include(export_urls, namespace="data_exports")),
    url(r'^publications/', include(publications_urls, namespace="publications")),
    url(r'^api/$', ApiPage.as_view(), name="api_home"),
    url(r'^api/', include(api.data_api.urls, namespace="data_api")),
    url(r'^explore/', include(explore_urls, namespace="explore")),
)\
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
