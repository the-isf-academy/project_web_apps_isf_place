from django.shortcuts import render, redirect
from .models import Tiles

def loading(request):
    return render(request, 'myapp/loading.html')

def index(request):
    grid = []
    for x in range(1, 21):  # Change this line
        row = []
        for y in range(1, 21):  # Change this line
            tile = Tiles.objects.filter(id=(x-1)*10+y).first()  # Change this line
            row.append(tile)
        grid.append(row)
    return render(request, 'myapp/index.html', {'grid': grid})

def leaderboard(request):
    return render(request, 'myapp/leaderboard.html')

def change_rgb(request, pk, r, g, b):
    tile = Tiles.objects.filter(id=pk).first()
    tile.changergb(r, g, b)
    return redirect('myapp:home')