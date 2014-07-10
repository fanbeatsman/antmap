from django.conf.urls import patterns, url
from bushstats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^stats$', views.stats, name='stats'),
    url(r'search', views.search, name='search'),
    url(r'stats_test', views.update_stats, name='stats_test'),
)
