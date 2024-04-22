from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone


#### class based views

class IndexView(TemplateView):
    template_name = "myapp/index.html"

