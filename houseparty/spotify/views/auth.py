from rest_framework import views, status
from rest_framework.response import Response
from requests import Request

from django.utils import timezone
from datetime import datetime, timedelta

from spotify.credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from spotify.serializers import SpotifyTokenSerializer
from spotify.utils import get_spotify_access_token, refresh_spotify_token



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

        key_expire_time = datetime.isoformat(datetime.now() + timedelta(seconds=callback_response.get('expires_in')))

        serializer = SpotifyTokenSerializer(data={
            'profile': request.user.profile.pk, 
            'expires_in': key_expire_time,
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

            response = refresh_spotify_token(spotify_connection.refresh_token)

            key_expire_time = datetime.isoformat(datetime.utcnow() + timedelta(seconds=response.get('expires_in')))

            spotify_connection.access_token = response.get('access_token')
            spotify_connection.token_type = response.get('token_type')
            spotify_connection.expires_in = key_expire_time
            spotify_connection.save()

            return Response(status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


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

        spotify_is_authenticated = False
        key_is_available = False

        if spotify_access_token and spotify_refresh_token is not None:
            spotify_is_authenticated = True

        if spotify_key_expire is not None and datetime.isoformat(spotify_key_expire) > datetime.isoformat(datetime.utcnow()):
            key_is_available = True
        
        context = {
            'spotify_is_authenticated': spotify_is_authenticated,
            'key_is_available': key_is_available
        }

        return Response(context, status=status.HTTP_200_OK)