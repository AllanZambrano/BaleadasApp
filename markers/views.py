from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Marker
from .forms import MarkerForm
from django.contrib.messages.views import SuccessMessageMixin


class Map(ListView):
    model = Marker
    template_name = 'map.html'

class CreateEntry(SuccessMessageMixin,CreateView):
    form_class = MarkerForm
    template_name = 'add.html'
    success_message = "Marker was created successfully"
    success_url = reverse_lazy('map')
