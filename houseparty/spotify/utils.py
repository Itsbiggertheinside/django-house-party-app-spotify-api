from requests import post
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI



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