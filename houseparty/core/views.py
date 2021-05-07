from rest_framework import status, viewsets, mixins, permissions, pagination
from rest_framework.response import Response

from .serializers import RoomSerializer
from .permissions import ListCreateOrIsOwner
from .models import Room


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('host').filter(is_locked=False).order_by('-created_at')
    serializer_class = RoomSerializer
    permission_classes = (ListCreateOrIsOwner, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'host': request.user.profile, **request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)