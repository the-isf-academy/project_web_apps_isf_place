from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Tiles

def index(request):
    Tiles_all = Tiles.objects.all()
    num_tiles = Tiles_all.count()
    return render(request, 'myapp/index.html', {'Tiles': Tiles_all, 'num_tiles': num_tiles})