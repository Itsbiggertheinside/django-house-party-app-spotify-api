from requests import post, put, get

from spotify.credentials import REQUEST_BASE_URL
from core.utils import safe_execute
from .token import check_key_is_available, update_profile_tokens



def get_available_devices(host_tokens):
    headers = { 'Content-Type': 'application/json', 'Authorization': f'{host_tokens.token_type} {host_tokens.access_token}' }
    response = get(REQUEST_BASE_URL + '/me/player/devices', headers=headers)
        
    return safe_execute(response.json())


def get_playlists(headers):
    response = get(REQUEST_BASE_URL + '/me/playlists', headers=headers)
    return safe_execute(response.json())


def get_tracks(headers, playlist_id):
    response = get(REQUEST_BASE_URL + '/playlists/{}/tracks'.format(playlist_id), headers=headers)
    return safe_execute(response.json())


def get_currently_playing(headers):
    response = get(REQUEST_BASE_URL + '/me/player/currently-playing', headers=headers)
    data = response.json()

    artist_string = ''
    for i, artist in enumerate(data.get('item').get('artists')):
        if i > 0:
            artist_string += ' & '
        artist_string += artist.get('name')

    current_song = {
        'artists': artist_string,
        'title': data.get('item').get('name'),
        'track_name': artist_string + ' - ' + data.get('item').get('name'),
        'duration_ms': data.get('item').get('duration_ms'),
        'progress_ms': data.get('progress_ms'),
        'is_playing': data.get('is_playing'),
        'song_id': data.get('item').get('id'),
    }

    return safe_execute(current_song)


def play_song(host_tokens, headers, playlist_id, song_offset):
    device = get_available_devices(host_tokens)['devices'][0]

    response = put(REQUEST_BASE_URL + '/me/player/play', headers=headers, json={
        'device_id': device['id'],
        'context_uri': 'spotify:playlist:' + playlist_id,
        'offset': { 'position': song_offset }, 
        'position_ms': 0
    })

    return get_currently_playing(headers)


def pause_song(headers):
    method = 'put'
    endpoint = '/me/player/pause'
    return


def next_song(headers):
    method = 'post'
    endpoint = '/me/player/next'
    return


def switch_request_type(type, host_tokens, headers, playlist_id, song_offset):
    if type == 'playlists':
        return get_playlists(headers)

    elif type == 'tracks':
        return get_tracks(headers, playlist_id)

    elif type == 'current_song':
        return get_currently_playing(headers)

    elif type == 'play_song':
        return play_song(host_tokens, headers, playlist_id, song_offset)

    elif type == 'pause_song':
        return pause_song(headers)

    elif type == 'next_song':
        return next_song(headers)


def execute_spotify_request(host_tokens, type, playlist_id=None, song_offset=None):

    headers = {'Content-Type': 'application/json', 'Authorization': f'{host_tokens.token_type} {host_tokens.access_token}'}
    key_is_available = check_key_is_available(host_tokens.expires_in)
    
    if key_is_available:
        return switch_request_type(type, host_tokens, headers, playlist_id, song_offset)
    else:
        update_token = update_profile_tokens(host_tokens)
        return switch_request_type(type, headers, playlist_id, song_offset) if update_token else None