from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'data.content.import_export.export', name="exports"),
    url(r'^(?P<year>\d{4})/$',
        'data.content.import_export.export_for_year', name="export_by_year"),
    url(r'^(?P<year>\d{4})/(?P<destination>[\w\-]+)/$',
        'data.content.import_export.export_for_year' ,
        name="export_by_year_by_destination"),
    url(r'^search/$', 'data.content.import_export.export_search',
        name="export_search"),
    url(r'^(?P<item>[\w\-]+)/$',
        'data.content.import_export.export_by_item' ,
        name="export_by_item"),
    url(r'^(?P<item>[\w\-]+)/(?P<destination>[\w\-]+)/$',
        'data.content.import_export.export_by_item' ,
        name="import_by_item_destination"),


)
