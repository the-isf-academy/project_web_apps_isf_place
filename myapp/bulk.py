from myapp.models import Tiles
for i in range(500): 
    tile = Tiles(r=255, g=255, b=255, house='A')
    tile.save()