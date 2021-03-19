from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    host = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Room
        fields = '__all__'