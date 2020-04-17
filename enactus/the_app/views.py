from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.

def home(request):
	aboutEnactus = AboutEnactus.objects.get(id=1)
	projects = Projects.objects.all()
	contact = Contact.objects.get(id=1)

	context = {'aboutEnactus':aboutEnactus, 'projects': projects, 'contact': contact}

	return render(request, 'index.html', context)


# def about(request):
#     aboutEnactus = AboutEnactus.objects.get(id=1)
#     return render(request, 'about.html', {'aboutEnactus': aboutEnactus})

# def render_projects(request):
#     projects = AboutEnactus.objects.all()
#     return render(request, 'projects.html', {'projects': projects})