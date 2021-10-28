  
from rest_framework import serializers
from .models import Artist, Member
from albums.serializers import AlbumShallowSerializer

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = AlbumShallowSerializer(many=True, read_only=True)
    class Meta:
        model = Artist # the model that the serialzer is based on
        fields = (
            "id",
            "name",
            "members",
            # Important bit: these "reverse" relationships weren't included when we had "__all__"
            "albums",
        )
        # Important bit: depth
        depth = 2

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member # the model that the serialzer is based on
        fields = (
            "id",
            "name",
            "date_of_birth",
            # Important bit: these "reverse" relationships weren't included when we had "__all__"
            "artists",
        )
        depth = 1


# can also use fields = ['title', 'artist', 'cover_image']