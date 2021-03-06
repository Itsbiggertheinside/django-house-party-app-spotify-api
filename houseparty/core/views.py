from rest_framework import status, viewsets, mixins, permissions, pagination

from .serializers import ProfileSerializer, RoomSerializer
from .permissions import ListCreateOrIsOwner
from .models import Profile, Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('host__user').filter(is_locked=False).order_by('-created_at')
    serializer_class = RoomSerializer
    permission_classes = (ListCreateOrIsOwner, )

    def perform_create(self, serializer):
        profile = self.request.user.profile
        room = profile.room_set.first()

        if serializer.is_valid():
            if not room:
                serializer.save(host=profile)