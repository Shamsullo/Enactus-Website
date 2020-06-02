from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

from .forms import MessageForm
from .models import *


# Create your views here.

def home(request):
    # aboutEnactus = AboutEnactus.objects.get(id=1)
    # projects = Projects.objects.all()
    # contact = Contact.objects.get(id=1)

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

    # context = {'aboutEnactus': aboutEnactus,
    #            'projects': projects, 'contact': contact,
    #            'form': form}

    # if request.method == 'POST':
    # message = request.POST['message']

    return render(request, 'index.html', )


# def about(request):
#     aboutEnactus = AboutEnactus.objects.get(id=1)
#     return render(request, 'about.html', {'aboutEnactus': aboutEnactus})

# def render_projects(request):
#     projects = AboutEnactus.objects.all()
#     return render(request, 'projects.html', {'projects': projects})
