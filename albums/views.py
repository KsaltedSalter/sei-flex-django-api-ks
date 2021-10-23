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

# API handlers
def albums(request):
    if request.method == 'GET':
        return read(request)
    if request.method == 'POST':
        return create(request)

def album(request):
    if request.method == 'GET':
        return read_one(request)
    if request.method == 'PATCH':
        return update(request)
    if request.method == 'DELETE':
        return delete(request)

# CRUD
def create(request):
    return HttpResponse('CREATE')

def read(request):
    return HttpResponse('READ')

def read_one(request):
    return HttpResponse('READ ONE')

def update(request):
    return HttpResponse('UPDATE')

def delete(request):
    return HttpResponse('DELETE')