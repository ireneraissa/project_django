from django.shortcuts import render
from django.views import generic
#from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse

import stripe
from django.shortcuts import redirect
from . import models
from .models import Caracteristic, Info, Bus
from . import forms 


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index. keep going")

class HomeView(generic.ListView):
	template_name='bus_gestion/home.html'
	context_object_name = 'latest_list_bus_list'
	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""

		return Bus.objects.all()
		return Info.objects.all()[8:10]



class DetailView(generic.ListView):
    model= Info
    template_name='bus_gestion/detail.html'
    context_object_name = 'latest_list_bus_list'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Info.objects.all()




class DriverView(generic.DetailView):
    model= Caracteristic
    template_name='bus_gestion/driver.html'

# # Create your views here.
