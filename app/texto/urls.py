from django.urls import path
from .views import search_music, search_singer

urlpatterns = [
    path('musics', search_music, name='search_music'),
    path('singers', search_singer, name='search_singer'),
]
