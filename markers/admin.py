from django.contrib import admin
from django.contrib.gis.db import models
from leaflet.admin import LeafletGeoAdmin
from .models import Marker



class MarkerAdmin(LeafletGeoAdmin):
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ['name', ]

admin.site.register(Marker, MarkerAdmin)

