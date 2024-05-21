from django.db import models

# Create your models here.
class Tiles(models.Model):
    r = models.IntegerField()
    g = models.IntegerField()
    b = models.IntegerField()
    DIFFICULTY_CHOICES = [
        ('F', 'Fire'),
        ('W','Wood'),
        ('M', 'Metal'),
        ('E', 'Earth'),
        ('T', 'Water'),
        ('A', 'Admin'),
    ]

    house = models.CharField(
        max_length=1,
        choices=DIFFICULTY_CHOICES,
        default=None,
    )

    def change_rgb(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.save()

