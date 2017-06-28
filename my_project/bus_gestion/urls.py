from django.conf.urls import url
from . import views

app_name = 'bus_gestion'

urlpatterns= [
	url(r'^$', views.index, name='index'),	
	url(r'^chauffeur/$', views.DriverListView.as_view(), name='chauffeur'),
   # url(r'^chauffeur/(?P<pk>\d+)$', views.DriverView.as_view(), name='chauffeur-detail'),
]
