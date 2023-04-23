from django.urls import path, include
from .views import search_singer

urlpatterns = [
    path('', search_singer),
]
