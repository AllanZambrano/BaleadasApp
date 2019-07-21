from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Marker


@admin.register(Marker)
class MarkerAdmin(OSMGeoAdmin):
    list_display = ['name', 'point', 'longitude', 'latitude']
    search_fields = ['name']
    default_lat = 1582501.1690300864
    default_lon = -9706180.173196191
    default_zoom = 12
