from bs4 import BeautifulSoup
import requests
import os
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import quote

# BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIFY_BASE_URL = "https://api.spotify.com/v1"
SPOTIFY_ME_ENDPOINT = f"{SPOTIFY_BASE_URL}/me"
SPOTIFY_USERS_ENDPOINT = f"{SPOTIFY_BASE_URL}/users"
SPOTIFY_SEARCH_ENDPOINT = f"{SPOTIFY_BASE_URL}/search"
SPOTIFY_PLAYLISTS_ENDPOINT = f"{SPOTIFY_BASE_URL}/playlists"
redirect_uri = "http://localhost:3000"


def get_target_playlist_id(user_playlists, playlist_name):
    filtered = [playlist["id"] for playlist in user_playlists if playlist_name == playlist["name"]]
    if len(filtered) > 0:
        return filtered[0]
    return None


user_date = input("Which year do you want to travel to? (Type date in 'YYYY-MM-DD' format): ")
playlist_generated_name = f"{user_date} | 5 Hottest Songs"

# target_url = f"{BILLBOARD_BASE_URL}/{user_date}"
# hot_songs_response = requests.get(target_url)
# hot_songs_html = hot_songs_response.text
# soup = BeautifulSoup(hot_songs_html, "html.parser")
# hot_song_elements = soup.select("h3#title-of-a-story")
# hot_song_titles = [element.getText() for element in hot_song_elements]

mocked_songs_data = [
    {"title": "Foolish", "artist": "Ashanti"},
    {"title": "I Need A Girl (Part One)", "artist": "P. Diddy"},
    {"title": "What's Luv?", "artist": "Fat Joe"},
    {"title": "U Don't Have To Call", "artist": "Usher"},
    {"title": "A Thousand Miles", "artist": "Vanessa Carlton"},
    {"title": "Without Me", "artist": "Eminem"},
    {"title": "Hot in Herre", "artist": "Nelly"}
]

sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=redirect_uri,
                        scope="user-read-private"
                              " user-read-email"
                              " playlist-modify-private"
                              " playlist-modify-public")

access_token = sp_oauth.get_access_token(as_dict=False)

headers = {
    'Authorization': f'Bearer {access_token}'
}

user_response = requests.get(SPOTIFY_ME_ENDPOINT, headers=headers)
user_data = user_response.json()
user_id = user_data["id"]

user_playlists_endpoint = f"{SPOTIFY_USERS_ENDPOINT}/{user_id}/playlists"

playlists_response = requests.get(user_playlists_endpoint, headers=headers)
playlists_response.raise_for_status()
playlists_data = playlists_response.json()

target_playlist_id = get_target_playlist_id(playlists_data["items"], playlist_generated_name)

if target_playlist_id is None:
    data = {
        "name": playlist_generated_name,
        "description": "Automatically created list for 100 Hottest hits",
        "public": True
    }

    create_playlist_response = requests.post(user_playlists_endpoint, json=data, headers=headers)
    create_playlist_response.raise_for_status()
    create_playlist_data = create_playlist_response.json()
    target_playlist_id = create_playlist_data["id"]


song_uris = []
for mocked_song_data in mocked_songs_data:
    params = {
        "q": f"track:{mocked_song_data["title"]} artist: {mocked_song_data["artist"]}",
        "type": "track",
        "market": "US"
    }

    available_songs_response = requests.get(f"{SPOTIFY_SEARCH_ENDPOINT}", params=params, headers=headers)
    available_songs_response.raise_for_status()
    available_songs_data = available_songs_response.json()

    if len(available_songs_data["tracks"]["items"]) > 0:
        relevant_songs = [song_data for song_data in available_songs_data["tracks"]["items"]
                          if song_data["name"] == mocked_song_data["title"]]

        if len(relevant_songs) > 0:
            target_song = relevant_songs[0]

            if "uri" in target_song:
                song_uris.append(target_song["uri"])

if len(song_uris) > 0:
    data = {
        "uris": song_uris
    }

    add_songs_response = requests.post(
        f"{SPOTIFY_PLAYLISTS_ENDPOINT}/{target_playlist_id}/tracks",
        json=data,
        headers=headers
    )
    add_songs_response.raise_for_status()
    add_songs_data = add_songs_response.json()
    print("Available songs were added to a playlist")
else:
    print("Unable to add songs to the playlist as they are not found...")
