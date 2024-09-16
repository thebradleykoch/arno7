# Spotify AI Playlist Generator

import requests
import base64

# set client_id and client_secret
client_id = "516f93038bd346d58efba24e400a9695"
client_secret = "673da0f02d044bc895e8e53dc908a8a6"

# request an access token
token_url = "https://accounts.spotify.com/api/token"

token_data = {
    "grant_type": "client_credentials"
}

token_headers = {
    "Authorization": f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(token_url, data=token_data, headers=token_headers)
access_token = response.json()["access_token"]


# Getting the song's metadata
song_uri = "0jkiOZCb3yToykDRAtLHdT"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

url = f"https://api.spotify.com/v1/tracks/{song_uri}"

response = requests.get(url, headers=headers)

song_metadata = response.json()
artist = song_metadata["artists"][0]["name"]
album = song_metadata["album"]["name"]
try:
    genre = song_metadata["album"]["genres"][0]
except KeyError:
    genre = None


# Using song's metadata to find similar songs
similar_songs_url = f"https://api.spotify.com/v1/recommendations?seed_artists={artist}&seed_genres={genre}&seed_tracks={song_uri}&limit=10"

response = requests.get(similar_songs_url, headers=headers)
similar_songs = response.json()["tracks"]


# Creating the playlist
playlist_name = f"{artist} AI Radio"

playlist_url = "https://api.spotify.com/v1/me/playlists"

playlist_data = {
    "name": playlist_name,
    "description": f"An AI radio station based on the song {song_metadata['name']} by {artist}",
    "public": False
}

response = requests.post(playlist_url, json=playlist_data, headers=headers)
playlist_id = response.json()["id"]

# Adding the songs to the playlist
song_uris = [song["uri"] for song in similar_songs]
add_songs_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

add_songs_data = {
    "uris": song_uris
}

response = requests.post(add_songs_url, json=add_songs_data, headers=headers)
