from rest_framework import views, status
from rest_framework.response import Response
from requests import Request

from spotify.credentials import CLIENT_ID, REDIRECT_URI
from spotify.serializers import SpotifyTokenSerializer
from spotify.utils import get_spotify_access_token, update_profile_tokens, get_available_devices, convert_key_expire_time



# Create your views here.
class AuthURL(views.APIView):

    def get(self, request, *args, **kwargs):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)


class SpotifyCallback(views.APIView):

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        callback_response = get_spotify_access_token(code)

        serializer = SpotifyTokenSerializer(data={
            'profile': request.user.profile.pk, 
            'expires_in': convert_key_expire_time(callback_response.get('expires_in')),
            'access_token': callback_response.get('access_token'),
            'refresh_token': callback_response.get('refresh_token'),
            'token_type': callback_response.get('token_type')
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SpotifyRefreshToken(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            spotify_connection = request.user.profile.spotifytoken
            update_profile_tokens(spotify_connection)
            return Response(status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SpotifyDevices(views.APIView):

    def get(self, request, *args, **kwargs):
        devices = get_available_devices(request.user.profile.spotifytoken)
        return Response(devices, status=status.HTTP_200_OK)