# Shameless copy of https://github.com/valeriangalliat/spotify-buddylist, except translated to python because who likes node.js
import requests


def get_web_access_token(spdc_cookie: str) -> str:
    res = requests.get(
        "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
        headers={"Cookie": f"sp_dc={spdc_cookie}"})
    return res.json()["accessToken"]


def get_friend_activity(web_access_token: str) -> dict:
    res = requests.get(
        "https://guc-spclient.spotify.com/presence-view/v1/buddylist",
        headers={"Authorization": f"Bearer {web_access_token}"}
    )
    return res.json()
