from rest_framework import viewsets, mixins, permissions, pagination

from .serializers import ProfileSerializer, RoomSerializer
from .models import Profile, Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('host__user').filter(is_locked=False).order_by('-created_at')
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(host=profile)