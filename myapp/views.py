from django.shortcuts import render, redirect
from .models import Tiles

def loading(request):
    return render(request, 'myapp/loading.html')
# Change how this is sent to the html. Should send all objects!
def index(request):
    grid = []
    for x in range(1, 21):  # Change this line
        row = []
        for y in range(1, 21):  # Change this line
            tile = Tiles.objects.filter(id=(x-1)*20+y).first()
            row.append(tile)
        grid.append(row)
    return render(request, 'myapp/index.html', {'grid': grid})
def leaderboard(request):
    return render(request, 'myapp/leaderboard.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_color(request, pk):
    print("updated_color")
    if request.method == 'POST':
        data = json.loads(request.body)
        r = data.get('r')
        g = data.get('g')
        b = data.get('b')

        # Update the color data in the database
        # Assuming you have a Tile object to update
        tile = Tiles.objects.get(id=pk)  # Replace with your own query
        tile.r = r
        tile.g = g
        tile.b = b
        tile.save()

        return JsonResponse({'status': 'success'})