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

    # <img width="300" src="${props.picture_url}"/><h3>${props.title}</h3><p>${props.description}</p>