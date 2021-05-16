from requests import post, get

from rest_framework import status
from rest_framework.response import Response

from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, REQUEST_BASE_URL



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


def switch_spotify_request_type(type, playlist_id=None):
    method = ''
    endpoint = ''

    if type == 'playlists':
        method = 'get'
        endpoint = '/me/playlists'

    if type == 'tracks':   
        method = 'get'
        endpoint = '/playlists/{}/tracks'.format(playlist_id)

    elif type == 'currently_song':
        method = 'get'
        endpoint = '/me/currently-playing'

    elif type == 'play_song':
        method = 'put'
        endpoint = '/me/player/play'

    elif type == 'pause_song':
        method = 'put'
        endpoint = '/me/player/pause'

    elif type == 'repeat_song':
        method = 'put'
        endpoint = '/me/player/repeat'

    elif type == 'shuffle_playlist':
        method = 'put'
        endpoint = '/me/player/shuffle'

    elif type == 'next_song':
        method = 'post'
        endpoint = '/me/player/next'

    elif type == 'previous_song':
        method = 'post'
        endpoint = '/me/player/previous'

    return { 'method': method, 'endpoint': endpoint }


def execute_spotify_api_request(host_tokens, endpoint, method):

    headers = { 'Content-Type': 'application/json', 'Authorization': f'{host_tokens.token_type} {host_tokens.access_token}' }
    response = {}
    
    if method == 'get':
        response = get(REQUEST_BASE_URL + endpoint, headers=headers)
    # elif method == 'post':
    #     response = get(REQUEST_BASE_URL + endpoint, headers=headers)

    try:
        return response.json()
    except Exception as e:
        return {'error': 'Issue with request {}'.format(e)}