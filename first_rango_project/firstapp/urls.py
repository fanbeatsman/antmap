from django.conf.urls import patterns, url
from firstapp import views 

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^stats_test/$', views.update_stats, name='stats_test'),
	url(r'^picture_game/$', views.profile_picture_game, name='picture_game'),
)


