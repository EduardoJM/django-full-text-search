from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import search_music, search_singer
from .viewsets import SingerViewSet

router = SimpleRouter()
router.register("singer", SingerViewSet, "Singer")

urlpatterns = [
    path('musics', search_music, name='search_music'),
    path('singers', search_singer, name='search_singer'),
    path('api/', include(router.urls))
]
