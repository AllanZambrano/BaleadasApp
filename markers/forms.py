from mapwidgets.widgets import GooglePointFieldWidget
from django import forms
from .models import Marker

class MarkerForm(forms.ModelForm):
    class Meta:
        model = Marker
        fields = ("name", "point")
        widgets = {
            'point': GooglePointFieldWidget,
        }