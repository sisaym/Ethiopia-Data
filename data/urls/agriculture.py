from django.conf.urls import patterns, include, url

from ..content import agriculture

urlpatterns = patterns('',
    # Agricultural statistics
    url(r'^$', 'data.content.agriculture.agricultural_production', name="agriculture"),
    url(r'^national/$','data.content.agriculture.get_national_data', name="national_data"),
    url(r'^regional/$','data.content.agriculture.get_regional_data', name="regional_data"),
    url(r'^search/$', 'data.content.agriculture.agricultural_production_search',
        name="agriculture_search"),
    url(r'^(?P<year>\d{4})/$',
        'data.content.agriculture.agricultural_production',
        name="agriculture_by_year"),

    url(r'^(?P<sub_group>[\w\-]+)/$',
        'data.content.agriculture.agricultural_production',
        name="agriculture_by_sub_group"),
    url(r'^(?P<year>\d{4})/(?P<sub_group>[\w\-]+)/$',
        'data.content.agriculture.agricultural_production',
        name="agriculture_by_year_crop"),
)
