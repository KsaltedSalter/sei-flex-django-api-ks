from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album # the model that the serialzer is based on
        fields = '__all__' # the fields to include in the serilazation - this is the python way



# can also use fields = ['title', 'artist', 'cover_image']