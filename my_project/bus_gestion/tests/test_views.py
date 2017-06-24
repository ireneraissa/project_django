import pytest
from django.http import Http404
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mock import patch
from mixer.backend.django import mixer
from django.shortcuts import render
from .. import views

pytestmark = pytest.mark.django_db

class TestHomeViews:
	def test_anonymous(self):
		req=RequestFactory().get('/')

		resp=views.HomeView.as_view()(req)
		assert resp.status_code==200, 'should be callable by anyone '


class TestCaracteristicUpdateView:

	def test_get(self):
		req=RequestFactory().get('/')
		req.user=AnonymousUser()
		obj=  mixer.blend('bus_gestion.Caracteristic')
		resp=views.CaracteristicUpdateView.as_view()(req, pk=obj.pk)
		assert resp.status_code ==200, 'should be callable by anyone'

	def test_post(self):

		post=mixer.blend('bus_gestion.Caracteristic')
		data={'name': 'aims','surname':'chantle', 'tel' : 771710298}
		req=RequestFactory().post('/', data=data)
		req.user=AnonymousUser()
		resp=views.CaracteristicUpdateView.as_view()(req, pk=post.pk)
		assert resp.status_code == 302, 'should redirect to success view'
		post.refresh_from_db()
		assert post.name == 'aims', 'Should update the post'


# def test_CHAUFFEUR(request):
# 	#req=demande()
# 	req=render(request, 'bus_gestion/caracteristic.html', {})

# 	assert req.status_code==404, 'should call us to create a template'
# 	#class TestDetailsView


