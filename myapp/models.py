from django.db import models

# Create your models here.
class Tiles(models.Model):
    r = models.IntegerField()
    g = models.IntegerField()
    b = models.IntegerField()
    house = models.CharField(max_length=1)

    def change_rgb(self,id,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.save()

