from rest_framework.viewsets import ModelViewSet
from singers.models import Singer
from singers.serializers import SingerSerializer
from search.filters import FullTextSearchFilter

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    filter_backends = [FullTextSearchFilter]
    search_config = "portuguese"
    search_fields = ["name"]
    similarity_threshold = 0.3
