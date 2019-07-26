# from mapwidgets.widgets import GooglePointFieldWidget
# from django import forms
# from .models import Marker
#
# class MarkerForm(forms.ModelForm):
#     class Meta:
#         model = Marker
#         fields = ("name", "geom")
#         widgets = {
#             'geom': GooglePointFieldWidget,
#         }

from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Marker

class MarkerForm(forms.ModelForm):

    class Meta:
        model = Marker
        fields = ('name', 'geom')
        widgets = {'geom': LeafletWidget()}