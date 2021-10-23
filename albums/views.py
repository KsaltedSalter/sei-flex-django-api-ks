from django.shortcuts import render
from django.http import HttpResponse

from .models import Album

# Create your views here.
def index(request):
    # grabbing what you need from the database
    list = Album.objects.all
    # creating a context object
    context = {'albums': list}

    # rendering based on a template
    return render(request, 'albums/index.html', context)

    # add this first - return HttpResponse("HELLO WORLD")