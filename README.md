# Spotify Playlist

Given a date, scrape Billboard Top 100 and create a Spotify playlist. 
Python Bootcamp Day 46


## Usage
Using Beautiful Soup and SpotiPY, you can create a public or private playlist by
scraping the Billboard Top 100 for your chosen week.

To install modules used in this project, run this in your terminal:

`pip install -r requirements.txt` 

You will need [Developer rights from Spotify(https://developer.spotify.com/dashboard/)].

A few gotchas that had to be worked through:

1. When you set the scope in SpotiPY, if the playlist is going to be private you
will need to also add in `playlist-modify` so your scope will be:

`"playlist-modify-private, playlist-modify"`

See [Stack Overflow](https://stackoverflow.com/questions/24288905/spotify-web-api-client-scope-not-working) for info on this.

2. On line 79 when you add songs to the new Playlist, you'll see:

`new_playlist["id"]`

When you create a playlist, if you print the output, you'll get an ID, but it's
not THIS ID. I kept trying to add songs, and nothing would error, but no songs
would get added. 

It's buried in the Spotify API docs, but if you look at the [response example](https://developer.spotify.com/documentation/web-api/reference/#/operations/create-playlist), there is an ID that is not part of a list.
The above code will reference that ID and tracks will successfully be added to 
your playlist.

3. As written, the code will create playlists every time it's run, even if it's
for the same date entry.





## License
[MIT](https://choosealicense.com/licenses/mit/)