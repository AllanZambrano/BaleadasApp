from django.urls import path
from .views import Map, CreateEntry
from djgeojson.views import GeoJSONLayerView
from .models import Marker

urlpatterns = [
    path('', Map.as_view(), name='index'),
    path('new/', CreateEntry.as_view(), name='add_entry'),
    path('data.geojson/', GeoJSONLayerView.as_view(model=Marker), name='data'),
]
