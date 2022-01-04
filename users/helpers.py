import requests
import os


def api_fetch_token(data):
    url = os.environ.get("BASE_URL")
    response = requests.post(
        f"{url}o/token/",
        data=data,
        auth=(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET")),
    )
    response.raise_for_status()

    return response.json()
