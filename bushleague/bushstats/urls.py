from django.conf.urls import patterns, url
from bushstats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
#    url(r'stats', views.stats, name='stats'))
)
