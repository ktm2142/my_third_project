import requests
from django.conf import settings


BASE_URL = "http://dataservice.accuweather.com"


def get_location_key(city_name):
    url = f"{BASE_URL}/locations/v1/cities/search"
    params = {
        "apikey": settings.ACCUWEATHER_API_KEY,
        "q": city_name
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[0]["Key"] if data else None
    # if data and isinstance(data, list) and len(data) > 0:
    #     return data[0]["Key"]
    # return None


def get_current_conditions(location_key):
    url = f"{BASE_URL}/currentconditions/v1/{location_key}"
    params = {
        "apikey": settings.ACCUWEATHER_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json() if response.json() else None


def get_5_day_forecast(location_key):
    url = f"{BASE_URL}/forecasts/v1/daily/5day/{location_key}"
    params = {
        "apikey": settings.ACCUWEATHER_API_KEY,
        "metric": "true"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("DailyForecasts", [])
