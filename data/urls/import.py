from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
#     Import URLS
    url(r'^$', 'data.content.import_export.import_data',
        name="imports"),
    url(r'^(?P<year>\d{4})/$',
        'data.content.import_export.import_for_year', name="import_by_year"),
    url(r'^(?P<year>\d{4})/(?P<origin>[\w\-]+)/$',
        'data.content.import_export.import_for_year' ,
        name="import_by_year_by_origin"),
    url(r'^search/$', 'data.content.import_export.import_search',
        name="import_search"),
    url(r'^search2/$', 'data.content.import_export2.import_search',
        name="import_search"),
    url(r'^(?P<item>[\w\-]+)/$',
        'data.content.import_export.import_by_item' ,
        name="import_by_item"),
    url(r'^(?P<item>[\w\-]+)/(?P<origin>[\w\-]+)/$',
        'data.content.import_export.import_by_item' ,
        name="import_by_item_origin"),

)
