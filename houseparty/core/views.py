from rest_framework import status, viewsets, views
from rest_framework.response import Response

from django.utils import timezone

from .serializers import RoomSerializer
from .permissions import ListCreateOrIsOwner
from .models import Room

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = (ListCreateOrIsOwner, )
    lookup_field = 'code'

    def get_queryset(self):
        queryset = Room.objects.select_related('host__user', 'player', 'listener').prefetch_related('player__skip_votes__user', 'listener__active_users__user')

        if self.action == 'list':
            queryset.order_by('-created_at')

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'host': request.user.profile.pk, **request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ControlCenterAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        spotify_connection = None
        spotify_access_token = None
        spotify_refresh_token = None 
        spotify_key_expire = None

        try:
            spotify_connection = profile.spotifytoken
            spotify_access_token = spotify_connection.access_token
            spotify_refresh_token = spotify_connection.refresh_token
            spotify_key_expire = spotify_connection.expires_in
        except Exception as e:
            print(e)
        
        context = {
            'spotify_is_authenticated': True if spotify_access_token and spotify_refresh_token is not None else False,
            'key_is_available': True if spotify_key_expire is not None and spotify_key_expire > timezone.now() else False
        }

        return Response(context, status=status.HTTP_200_OK)