from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

from .forms import MessageForm
from .models import *


# Create your views here.

def home(request):
    aboutEnactus = AboutEnactus.objects.get(id=1)
    projects = Projects.objects.all()
    contact = Contact.objects.get(id=1)
    welcome = Welcome.objects.get(id=1)
    gallery = Gallery.objects.all()
    team = AcademicAdvisors.objects.all()

    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = form.cleaned_data
        form = MessageForm()

        msg = str('\n' + msg['name'] + ' has left the following message:\n\n'
                  + msg['subject']
                  + ':\n\n' + msg['message']
                  + '\n\nTel: ' + msg['phone_number'] +
                  '\nEmail: ' + msg['email'])

        send_mail('Notification from website',
                  str(msg),
                  settings.EMAIL_HOST_USER,
                  ['receiver email'],
                  fail_silently=False)

    context = {'aboutEnactus': aboutEnactus,
               'projects': projects, 'contact': contact, 'team': team,
               'welcome': welcome, 'form': form, 'gallery': gallery}

    # if request.method == 'POST':
    # message = request.POST['message']

    return render(request, 'index.html', context)


def projects(request):
    projects = Projects.objects.all()
    contact = Contact.objects.get(id=1)
    context = {'projects': projects, 'contact': contact}

    return render(request, 'projects.html', context)

def projects_details(request, project_id):
    project = Projects.objects.get(id=project_id)
    contact = Contact.objects.get(id=1)
    context = {'project': project, 'contact': contact}

    return render(request, 'project_detail.html', context)


def our_team(request):
    team = AcademicAdvisors.objects.all()
    contact = Contact.objects.get(id=1)
    context = {'team': team, 'contact': contact}

    return render(request, 'team.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    contact = Contact.objects.get(id=1)
    context = {'gallery': gallery, 'contact': contact}

    return render(request, 'gallery.html', context)

    