from rest_framework import serializers

from core.models import Profile
from .models import Player, Listener


class ProfileInstance(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'user_id': instance.id,
            'username': instance.user.username
        }


class PlayerSerializer(serializers.ModelSerializer):

    skip_votes = ProfileInstance(Profile.objects.select_related('user', 'spotifytoken'), many=True)

    class Meta:
        model = Player
        fields = ('current_song', 'skip_votes')


class ListenerSerializer(serializers.ModelSerializer):

    active_users = ProfileInstance(Profile.objects.select_related('user', 'spotifytoken'), many=True)

    class Meta:
        model = Listener
        fields = ('active_users',)