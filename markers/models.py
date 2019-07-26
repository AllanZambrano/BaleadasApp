from django.db import models
from django.contrib.gis.db import models

class Marker(models.Model):
    name = models.CharField(max_length=120)
    geom = models.PointField('Coordinates')

    @property
    def longitude(self):
        return self.geom[0]

    def latitude(self):
        return self.geom[1]

    def __str__(self):
        return self.name

    @property
    def popupContent(self):
      return self.name