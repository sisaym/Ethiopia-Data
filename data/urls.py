from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^exports/$', 'data.content.import_export.export', name="exports"),
    url(r'^exports/(?P<year>\d{4})/$',
        'data.content.import_export.export_for_year', name="export_by_year"),
    url(r'^exports/(?P<year>\d{4})/(?P<destination>[\w\-]+)/$',
        'data.content.import_export.export_for_year' ,
        name="export_by_year_by_destination"),
    url(r'^exports/search/$', 'data.content.import_export.export_search',
        name="export_search"),
    url(r'^exports/(?P<item>[\w\-]+)/$',
        'data.content.import_export.export_by_item' ,
        name="export_by_item"),
    url(r'^exports/(?P<item>[\w\-]+)/(?P<destination>[\w\-]+)/$',
        'data.content.import_export.export_by_item' ,
        name="import_by_item_destination"),


#     Import URLS   
    url(r'^imports/$', 'data.content.import_export.import_data',
        name="imports"),
    url(r'^imports/(?P<year>\d{4})/$',
        'data.content.import_export.import_for_year', name="import_by_year"),
    url(r'^imports/(?P<year>\d{4})/(?P<origin>[\w\-]+)/$',
        'data.content.import_export.import_for_year' ,
        name="import_by_year_by_origin"),
    url(r'^imports/search/$', 'data.content.import_export.import_search',
        name="import_search"),
    url(r'^imports/search2/$', 'data.content.import_export2.import_search',
        name="import_search"),
    url(r'^imports/(?P<item>[\w\-]+)/$',
        'data.content.import_export.import_by_item' ,
        name="import_by_item"),
    url(r'^imports/(?P<item>[\w\-]+)/(?P<origin>[\w\-]+)/$',
        'data.content.import_export.import_by_item' ,
        name="import_by_item_origin"),

    # Agricultural statistics
    url(r'^agriculture/$', 'data.content.agriculture.agricultural_production'
                           '', name="agriculture"),
    url(r'^agriculture/search/$',
        'data.content.agriculture.agricultural_production_search',
        name="agriculture_search"),
    url(r'^agriculture/(?P<year>\d{4})/$',
        'data.content.agriculture.agricultural_production',
        name="agriculture_by_year"),
    url(r'^agriculture/(?P<sub_group>[\w\-]+)/$',
        'data.content.agriculture.agricultural_production',
        name="agriculture_by_sub_group"),
    url(r'^agriculture/(?P<year>\d{4})/(?P<sub_group>[\w\-]+)/$',
        'data.content.agriculture.agricultural_production',
        name="agriculture_by_year_crop"),

    url(r'^test/$', 'data.content.import_export.test'),




)
