from django.conf.urls import url
from . import views

app_name = 'bus_gestion'

urlpatterns= [
	url(r'^$', views.index, name='index'),	
	url(r'^chauffeur/$', views.DriverListView.as_view(), name='chauffeur'),
	url(r'^bus/$', views.BusListView.as_view(), name='bus'),
	url(r'^bus/(?P<pk>[0-9]+)/$',views.DetailbusView.as_view(), name='detail_bus'),
	url(r'^driver/(?P<pk>[0-9]+)/$',views.DetaildriverView.as_view(), name='detail_chauffeur'),
	
	url(r'^bus_/$', views.HomeListView.as_view(), name='bus_bootstrap'),
	url(r'^new_driver/$', views.DriverCreate.as_view(), name='new_driver'),

	url(r'^new_bus/$', views.BusCreate.as_view(), name='new_bus'),
	url(r'^new_bus/$', views.BusCreate.as_view(), name='update'),
]
