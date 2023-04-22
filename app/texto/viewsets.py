from rest_framework.viewsets import ModelViewSet
from texto.models import Singer
from texto.serializers import SingerSerializer
from core.filters import FullTextSearchFilter

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    filter_backends = [FullTextSearchFilter]
    search_config = "portuguese"
    search_fields = ["name"]
    similarity_threshold = 0.3
