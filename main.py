from bs4 import BeautifulSoup
import requests
import spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
user_input_year = \
    input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")
URL = f" https://www.billboard.com/charts/hot-100/{user_input_year}"
CLIENT_ID = "31cb0de80017420fb7ffeeb0005e7152"
CLIENT_SECRET = "31773b91d0674f3dad30b1b930a2e195"
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
song_list_tags = soup.find_all(id="title-of-a-story",class_=["h3","c-title"])[6::4][:-4]
song_list = [song_tag.getText().strip() for song_tag in song_list_tags]
# user_id ="ey5m2np5bef7ztpahiz7j6ipdq?si=556d9c3dd98d4ca2"
print(len(song_list))
print(song_list)



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
