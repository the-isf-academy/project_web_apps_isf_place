from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Tiles

def index(request):
    grid = []
    for x in range(1, 101):
        row = []
        for y in range(1, 101):
            tile = Tiles.objects.filter(x_coordinates=x, y_coordinates=y).first()
            row.append(tile)
        grid.append(row)
    return render(request, 'myapp/index.html', {'grid': grid})