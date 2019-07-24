from django.urls import path
from .views import Map, CreateEntry

urlpatterns = [
    path('', Map.as_view(), name='map'),
    path('new/', CreateEntry.as_view(), name='add_entry'),
]
