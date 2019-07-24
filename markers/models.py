from django.db import models
from django.contrib.gis.db import models

class Marker(models.Model):
    name = models.CharField(max_length=120)
    point = models.PointField()

    @property
    def longitude(self):
        return self.point[0]

    def latitude(self):
        return self.point[1]

    def __str__(self):
        return self.name