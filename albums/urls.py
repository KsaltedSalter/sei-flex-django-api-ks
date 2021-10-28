from django.urls import path
from .views import AlbumDetailView, index, AlbumListView

urlpatterns = [
    path("", AlbumListView.as_view()),
    path("<int:id>/", AlbumDetailView.as_view()),
    path("view/", index),
] 