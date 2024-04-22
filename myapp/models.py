from django.db import models

# Create your models here.
class Tiles(models.Model):
    x_coordinates = models.IntegerField()
    y_coordinates = models.IntegerField()
    color = models.CharField(max_length=1)
    house = models.CharField(max_length=1)