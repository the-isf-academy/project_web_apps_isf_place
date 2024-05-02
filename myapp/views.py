from django.shortcuts import render, redirect
from .models import Tiles

def loading(request):
    return render(request, 'myapp/loading.html')

def index(request):
    grid = []
    for x in range(1, 101):
        row = []
        for y in range(1, 101):
            tile = Tiles.objects.filter(id=(x-1)*100+y).first()
            row.append(tile)
        grid.append(row)
    return render(request, 'myapp/index.html', {'grid': grid})

def leaderboard(request):
    return render(request, 'myapp/leaderboard.html')