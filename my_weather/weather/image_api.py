import requests
from django.conf import settings


def get_city_images(city_name):
    url = f"https://maps.googleapis.com/customsearch/v1"
    params = {
        "key": settings.GOOGLE_API_KEY,
        "cx": settings.GOOGLE_CSE_ID,
        "q": f"{city_name} city",
        "searchType": "image",
        "num": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "items" in data:
        return data["items"][0]["link"]
    else:
        return None
