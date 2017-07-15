from django.db import models
from geoposition.fields import GeopositionField


class City(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    year = models.DateField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=500)
    cities = models.ManyToManyField(City)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'