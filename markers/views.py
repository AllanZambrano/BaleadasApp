from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Marker
from .forms import MarkerForm


class Map(ListView):
    model = Marker
    template_name = 'map.html'

class CreateEntry(CreateView):
    form_class = MarkerForm
    template_name = 'add.html'
    success_url = reverse_lazy('map')
