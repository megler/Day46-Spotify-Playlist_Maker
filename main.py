# spotifyPlaylistMaker.py
#
# Python Bootcamp Day 46 - Spotify Playlist
# Usage:
#      Given a date, scrape Billboard Top 100 and create a Spotify playlist.
#
# Marceia Egler December 23, 2021

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests


load_dotenv()

spotify_client_id = os.getenv("spotify_client_id")
spotify_secret = os.getenv("spotify_secret")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=spotify_client_id,
        client_secret=spotify_secret,
        redirect_uri="http://localhost:8080",
        scope="playlist-modify-private, playlist-modify",
        show_dialog=True,
        cache_path=".cache",
    )
)
# Get spotify userid

user_id = sp.current_user()["id"]

# Scrape Songs

get_date = input("Enter the date you'd like to have songs for (YYYY-MM-DD): ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{get_date}/"
r = requests.get(billboard_url)
movies_webpage = r.text
soup = BeautifulSoup(movies_webpage, "html.parser")
titles = soup.find_all(
    "h3",
    id="title-of-a-story",
    class_="a-no-trucate",
)

songs = []

for title in titles:
    songs.append(title.text.strip())


# Create New Playlist


new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Top 100 Billboard for {get_date}",
    public=False,
    collaborative=False,
    description="Programatic Playlist",
)


# Add Songs To Playlist

songs_to_playlist = []
for song in songs:
    results = sp.search(q=song)
    try:
        get_uri = results["tracks"]["items"][0]["uri"]
        songs_to_playlist.append(get_uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


sp.playlist_add_items(playlist_id=new_playlist["id"], items=songs_to_playlist)
