from rest_framework import serializers

from core.models import Profile
from .models import Player


class SkipVotes(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'user_id': instance.id,
            'username': instance.user.username
        }


class PlayerSerializer(serializers.ModelSerializer):

    skip_votes = SkipVotes(Profile.objects.select_related('user'), many=True)

    class Meta:
        model = Player
        fields = ('current_song', 'skip_votes')