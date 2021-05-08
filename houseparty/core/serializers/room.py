from rest_framework import serializers
from core.models import Room


class RoomSerializer(serializers.ModelSerializer):

    host_username = serializers.CharField(source='host.user.username', read_only=True)

    class Meta:
        model = Room
        fields = '__all__'