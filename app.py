import buddy
from flask import Flask, url_for, render_template

spdc_cookie = "AQCzVVSFgZT2cLk_bKkoXc4-w9qU60KJN2WkKkRfxg5MmV3EBPGwwQ26B7DkoTFkAWZC3hcYvV3U5M99gE41gvGxR9IKnmbYsGktySFe2ErHtHUhUwQQJ0pwvseDHN-O7SfSpn2bcn3FVr8ihg5nja964UgRQ3Bs"
access_token = buddy.get_web_access_token(spdc_cookie)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/friends")
def friends():
    return render_template("friends.html", activity=update_activity())


@app.route("/me")
def personal_stats():
    return render_template("me.html")


@app.route("/raw")
def raw():
    return render_template("raw.html", activity=update_activity())


def update_activity():
    return buddy.get_friend_activity(access_token)["friends"]
