from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import RoomSerializer
from .permissions import ListCreateOrIsOwner
from .models import Room


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = (ListCreateOrIsOwner, )
    lookup_field = 'code'

    def get_queryset(self):
        queryset = Room.objects.select_related('host__user', 'player').prefetch_related('player__skip_votes__user')

        if self.action == 'list':
            queryset.order_by('-created_at')

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'host': request.user.profile.pk, **request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)