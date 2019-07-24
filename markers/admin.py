from django.contrib import admin
from django.contrib.gis.db import models
from .models import Marker
from mapwidgets.widgets import GooglePointFieldWidget



class MarkerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


admin.site.register(Marker, MarkerAdmin)

