from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album # the model that the serialzer is based on
        fields = '__all__' # the fields to include in the serilazation - this is the python way
        depth = 1

class AlbumShallowSerializer(serializers.ModelSerializer):
    class Meta:
        # the model that the serializer is based on
        model = Album
        # the fields to include in the serialization
        fields = "__all__"
        depth = 0

# can also use fields = ['title', 'artist', 'cover_image']