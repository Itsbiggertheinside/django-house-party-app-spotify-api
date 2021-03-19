from rest_framework import status, viewsets, mixins, permissions, pagination

from .serializers import RoomSerializer
from .permissions import ListCreateOrIsOwner
from .models import Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('host').filter(is_locked=False).order_by('-created_at')
    serializer_class = RoomSerializer
    permission_classes = (ListCreateOrIsOwner, )

    def perform_create(self, serializer):
        user = self.request.user

        if serializer.is_valid():
            serializer.save(host=user)