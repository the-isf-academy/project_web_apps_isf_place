from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Tiles

def index(request):
    tiles = list(Tiles.objects.all())
    grid = [tiles[i:i+100] for i in range(0, len(tiles), 100)]
    return render(request, 'myapp/index.html', {'grid': grid})

def leaderboard(request):
    return render(request, 'myapp/leaderboard.html',)