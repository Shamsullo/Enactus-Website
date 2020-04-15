from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.
def index(request):
    aboutEnactus = AboutEnactus.objects.all()
    return render(request, 'index.html', {'aboutEnactus': aboutEnactus})
