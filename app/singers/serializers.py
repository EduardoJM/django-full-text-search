from rest_framework import serializers
from singers.models import Singer

class SingerSerializer(serializers.ModelSerializer):
    rank = serializers.FloatField(read_only=True, default=0)
    similarity = serializers.FloatField(read_only=True, default=0)

    class Meta:
        model = Singer
        fields = "__all__"
