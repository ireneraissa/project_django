from django.conf.urls import url
from . import views

app_name = 'bus_gestion'

urlpatterns= [
	url(r'^$', views.HomeView.as_view(), name='home'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/driver/$', views.DriverView.as_view(), name='driver'),

]