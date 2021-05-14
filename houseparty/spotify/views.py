from rest_framework import views, status
from rest_framework.response import Response
from requests import Request, post

from datetime import datetime, timedelta

from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from .serializers import SpotifyTokenSerializer


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

        callback_response = post('https://accounts.spotify.com/api/token', data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }).json()

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