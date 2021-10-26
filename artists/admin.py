from django.contrib import admin

from artists.models import Artist, Member

# Register your models here.
admin.site.register(Artist)
admin.site.register(Member)