from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'^new/$', views.new, name='new'),
	url(r'^$', views.welcome, name='welcome'),
	url(r'^login$', views.login, name='login'),
	url(r'^register$', views.register, name='register'),
	url(r'^Dashboard/(?P<fid>[0-9]+)$', views.dashboard, name='dashboard'),
	url(r'^logout/(?P<fid>[0-9]+)$', views.logout, name='logout'),

	url(r'^update',views.update, name='update'),
	url(r'^maps/(?P<pid>[0-9]+)/$', views.maps, name='maps'),
	url(r'^madhu/(?P<pid>[0-9]+)/$', views.madhu, name='madhu'),
	url(r'ws_dashboard/(?P<pid>[0-9]+)/$', views.ws_dashboard, name='ws_dashboard'),
	url(r'wb_illustration/(?P<pid>[0-9]+)/$', views.wb_illustration, name='wb_illustration'),
	url(r'^soil/(?P<pid>[0-9]+)/$', views.soil, name='soil'),
	url(r'^wechart/$', views.wechart, name='wechart'),
	url(r'^wbchart/$', views.wbchart, name='wbchart'),

	url(r'control/(?P<pid>[0-9]+)/$',views.control, name='control'),
	url(r'addplant/(?P<fid>[0-9]+)/$',views.addplant, name='addplant'),


]