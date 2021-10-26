from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import views, response, status, exceptions

from albums.serializers import AlbumSerializer
from .models import Album

# Create your views here.
def index(request):
    # grabbing what you need from the database
    list = Album.objects.all()
    # creating a context object
    context = {'albums': list}

    # rendering based on a template
    return render(request, 'albums/index.html', context)

    # add this first - return HttpResponse("HELLO WORLD")

class AlbumListView(views.APIView):
    def get(self, _request):
        albums = Album.objects.all()
        serialized_albums = AlbumSerializer(albums, many=True)
        return response.Response(serialized_albums.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        album_to_add = AlbumSerializer(data=request.data)
        if album_to_add.is_valid():
            album_to_add.save()
            return response.Response(album_to_add.data, status=status.HTTP_201_CREATED)

        return response.Response(album_to_add.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetailView(views.APIView):
    def get_album_by_id(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            raise exceptions.NotFound(detail="Album does not exist")

    def get(self, _request, id):
        album = self.get_album_by_id(id)
        serialized_album = AlbumSerializer(album)
        return response.Response(serialized_album.data, status=status.HTTP_200_OK)

    def delete(self, _request, id):
        album = self.get_album_by_id(id)
        album.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        album = self.get_album_by_id(id)
        updated_album = AlbumSerializer(album, data=request.data)
        if updated_album.is_valid():
            updated_album.save()
            return response.Response(updated_album.data, status=status.HTTP_201_CREATED)
        return response.Response(updated_album.errors, status=status.HTTP_400_BAD_REQUEST) 









# WORKINGS OF WHAT NEEDS TO HAPPEN SUDO-CODE
# API handlers
# def albums(request):
#     if request.method == 'GET':
#         return read(request)
#     if request.method == 'POST':
#         return create(request)
# 
# def album(request):
#     if request.method == 'GET':
#         return read_one(request)
#     if request.method == 'PATCH':
#         return update(request)
#     if request.method == 'DELETE':
#         return delete(request)
# 
# CRUD
# def create(request):
#     return HttpResponse('CREATE')
# 
# def read(request):
#     return HttpResponse('READ')
# 
# def read_one(request):
#     return HttpResponse('READ ONE')
# 
# def update(request):
#     return HttpResponse('UPDATE')
# 
# def delete(request):
#     return HttpResponse('DELETE')