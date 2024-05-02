from django.db import models

# Create your models here.
class Tiles(models.Model):
    r = models.IntegerField()
    g = models.IntegerField()
    b = models.IntegerField()
    house = models.CharField(max_length=1)