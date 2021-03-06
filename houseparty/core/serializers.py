from rest_framework import serializers
from .models import Room, Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    host = ProfileSerializer(read_only=True)

    class Meta:
        model = Room
        fields = '__all__'