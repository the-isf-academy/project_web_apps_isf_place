from django.core.management.base import BaseCommand
from models import Tiles
import random

class Command(BaseCommand):
    help = 'Create random tiles'

    def handle(self, *args, **options):
        for x in range(1, 101):
            for y in range(1, 101):
              Object = Tiles(
                    x_coordinates=x,
                    y_coordinates=y,
                    r=random.randint(0, 255),
                    g=random.randint(0, 255),
                    b=random.randint(0, 255),
                    house=random.choice(['A', 'B', 'C', 'D', 'E'])
                )
              Object.save()