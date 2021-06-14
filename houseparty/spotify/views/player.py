from rest_framework import views, status, generics
from rest_framework.response import Response

from core.models import Room
from spotify.utils import execute_spotify_request


class PlayerAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        type = request.query_params.get('type')
        playlist_id = request.query_params.get('playlist')
        song_offset = request.query_params.get('song_offset')

        room = generics.get_object_or_404(Room, code=code)

        response = execute_spotify_request(room.host.spotifytoken, type, playlist_id, song_offset)

        return Response(response, status=status.HTTP_200_OK)