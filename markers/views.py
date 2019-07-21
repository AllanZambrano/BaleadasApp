from django.views.generic import ListView
from .models import Marker


class Map(ListView):
    model = Marker
    template_name = 'map.html'
