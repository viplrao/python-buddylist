from unicodedata import name
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import buddy
from flask import Flask, url_for, render_template

spdc_cookie = "REDACTED"
access_token = buddy.get_web_access_token(spdc_cookie)
app = Flask(__name__)
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/friends")
def friends():
    return render_template("friends.html", activity=get_activity())


@app.route("/me")
def personal_stats():
    return render_template("me.html")


@app.route("/raw")
def raw():
    return get_activity()


def get_activity():
    return buddy.get_friend_activity(access_token)["friends"]


def get_current_song_all() -> list:
    songs = []
    activity = get_activity()
    for user in activity:
        name = user["user"]["name"]


class Result:
    def __init__(self, uri, name) -> None:
        self.uri = uri
        self.name = name


class User(Result):
    def __init__(self, uri, name) -> None:
        super().__init__(uri, name)
