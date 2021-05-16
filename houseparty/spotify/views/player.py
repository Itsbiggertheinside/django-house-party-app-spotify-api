from rest_framework import views, status, generics
from rest_framework.response import Response

from core.models import Room
from spotify.utils import execute_spotify_api_request, switch_spotify_request_type


class PlayerAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        type = request.query_params.get('type')
        playlist = request.query_params.get('playlist', None)

        room = generics.get_object_or_404(Room, code=code)
        spotify_request_type = switch_spotify_request_type(type, playlist)

        print(spotify_request_type)

        response = execute_spotify_api_request(
            room.host.spotifytoken, spotify_request_type['endpoint'], spotify_request_type['method'])

        return Response(response, status=status.HTTP_200_OK)