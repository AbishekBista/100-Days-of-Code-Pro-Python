from bs4 import BeautifulSoup
import requests
from secret import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

# Set the billboard url for scrapping
date = input("Which year do you want to travel to? Enter the date in this format YYYY-MM-DD: ")
BILLBOARD_URL=f"https://www.billboard.com/charts/hot-100/{date}/"

# Get the HTML for scraping
response = requests.get(BILLBOARD_URL)
response.raise_for_status()
billboard_data = response.text

# Scrape the top 100 songs
soup = BeautifulSoup(billboard_data, 'html.parser')

songs = [song.string.replace("\t", "").replace("\n", "") for song in soup.select(selector="li > #title-of-a-story")]

# Get the current Spotify user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="playlist-modify-private"))

user = sp.current_user()

# Get the songs URI obtained after scraping
songs_uri = []
year = date.split("-")[0]
for song in songs:
    track_uri = sp.search(q=f'track:{song} year:{year}', type='track', market="NP")
    songs_uri.append(track_uri['tracks']['items'][0]['uri'])

# Create a Spotify playlist
playlist = sp.user_playlist_create(user=user['id'], name=f'{date} Billboard 100', public=False)
playlist_id = playlist['id']

# Add songs to playlist
sp.user_playlist_add_tracks(user=user['id'], playlist_id=playlist_id, tracks=songs_uri)






