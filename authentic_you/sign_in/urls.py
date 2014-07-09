from django.conf.urls import patterns, url

from sign_in import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout')
	url(r'^/add_user$', views.AddUser, name='add'),
	
)

	#url(r'^(?P<User_id>\d+)/$', views.UserView, name='user'),