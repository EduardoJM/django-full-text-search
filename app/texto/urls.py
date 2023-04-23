from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import search_music, search_singer
from .viewsets import SingerViewSet

router = SimpleRouter()
router.register("singer", SingerViewSet, "Singer")

urlpatterns = [
    path('musics', search_music, name='search_music'),
    path('singers', search_singer, name='search_singer'),
    path('api/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
