from django.conf.urls import url, patterns

from .views import PublicationsHome
urlpatterns = patterns('',
    url(r'^$',PublicationsHome.as_view(), name='home'),
)

