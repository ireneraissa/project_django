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



def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_bus=Bus.objects.all().count()
   
    num_chauffeur=Caracteristic.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
class HomeListView(generic.ListView):
    model=Bus
	template_name='bus_gestion/home.html'
	context_object_name = 'Bus_list'
	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""

		return Bus.objects.all()
    def get_context_data(self, **kwargs):

		#return Info.objects.all()[8:10]
        # Call the base implementation first to get a context
        context = super(HomeListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context



class DetailView(generic.DetailView):
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
