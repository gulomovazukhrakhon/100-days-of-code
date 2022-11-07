from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify
USERNAME = YOUR USERNAME
CLIENT_ID = YOUR SPOTIFY CLIENT ID
CLIENT_SECRET = YOUR SPOTIFY CLIENT SECRET
SONG_URI = "http://open.spotify.com/track/"

# Billboard
DATE = input("Which year do you want travel to? Type the date in that format YYYY-MM-DD: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{DATE}/"
YEAR = DATE.split('-')[0]

# Billboard
response = requests.get(BILLBOARD_URL) 
contents = response.text

soup = BeautifulSoup(contents, "html.parser") # Web Scraping
titles = soup.select(selector="ul li h3")
title_text = [title.getText().replace("\n", "").replace("\t", "") for title in titles]
del title_text[100:107]

# Spotipy
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = []

for track in title_text:
    result = sp.search(q=f"track:{track} year:{YEAR}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
