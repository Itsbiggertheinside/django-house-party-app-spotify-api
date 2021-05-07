from rest_framework import serializers
from core.models import Room


class RoomSerializer(serializers.ModelSerializer):

    host = serializers.SlugRelatedField(slug_field='user__username', read_only=True)

    class Meta:
        model = Room
        fields = '__all__'