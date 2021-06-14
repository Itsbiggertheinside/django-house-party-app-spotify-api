from requests import post
from datetime import datetime, timedelta

from spotify.credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI



def convert_key_expire_time(expires_in):
    key_expire_time = datetime.isoformat(datetime.utcnow() + timedelta(seconds=expires_in))
    return key_expire_time


def check_key_is_available(expire_time):
    key_is_available = datetime.isoformat(expire_time) > datetime.isoformat(datetime.utcnow())
    return key_is_available


def get_spotify_access_token(authorization_code):

    callback_response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    return callback_response


def refresh_spotify_token(refresh_token):

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    return response


def update_profile_tokens(host_tokens):

    response = refresh_spotify_token(host_tokens.refresh_token)
    key_expire_time = convert_key_expire_time(response.get('expires_in'))

    host_tokens.access_token = response.get('access_token')
    host_tokens.token_type = response.get('token_type')
    host_tokens.expires_in = key_expire_time
    host_tokens.save()

    return True