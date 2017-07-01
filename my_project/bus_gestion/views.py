from django.shortcuts import render
from django.views import generic
#from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bus_gestion.models import Driver
from django.urls import reverse_lazy
import stripe
from django.shortcuts import redirect
from . import models
from .models import Driver, Bus
from . import forms 
from .forms  import DriverForm
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index. keep going")

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_bus=Bus.objects.all().count()
   
    num_chauffeur=Driver.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'bus_gestion/index.html',
        context={'num_bus':num_bus,'num_chaufffeur':num_chauffeur}
    )



# # Create your views here.
class DriverListView(generic.ListView):
    model= Driver
    template_name='bus_gestion/chauffeur.html'
    context_object_name = 'chauffeur_list'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Driver.objects.all()
# # Create your views here.
class BusListView(generic.ListView):
    model= Bus
    template_name='bus_gestion/bus.html'
    context_object_name = 'bus_list'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Bus.objects.all()
# # Create your views here.
class DetaildriverView(generic.DetailView):
    model= Driver
    template_name='bus_gestion/detail_chauffeur.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Driver.objects.all()

class DetailbusView(generic.DetailView):
    model= Bus
    template_name='bus_gestion/detail_bus.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Bus.objects.all()

class DriverCreate(CreateView):
    model = Driver
    fields = ['name', 'surname', 'tel']
    template_name='bus_gestion/drivercreate.html'

class BusCreate(CreateView):
    model =Bus
    fields = ['nom_bus', 'numero_ligne', 'nombre_place', 'id_ecran']
    template_name='bus_gestion/buscreate.html'











class DriverUpdateView(generic.UpdateView):
    model=Driver
    template_name='bus_gestion/update_driver.html'
    form_class=forms.DriverForm
    success_url='/'
    def post(self, request, *args, **kwargs):
        if getattr(request.user, 'first_name', None) == 'martin':

            raise Http404()

        return super(DriverUpdateView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(DriverListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['some_data'] = 'This is just some data'
        return context


def driver_edit(request, pk):
    post = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        form = DriverForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = DriverForm(instance=post)
    return render(request, 'blog/driver_edit.html', {'form': form})


class HomeListView(generic.ListView):
    model=Bus
    template_name='bus_gestion/bus_.html'
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