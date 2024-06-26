from django.http import JsonResponse
from django.shortcuts import render

from .weather_api import get_current_conditions, get_location_key, get_5_day_forecast


def weather_view(request):
    city_name = request.GET.get('city')
    location_key = get_location_key(city_name)
    if location_key:
        current_conditions = get_current_conditions(location_key)[0]
        forecast = get_5_day_forecast(location_key)
        context = {
            'city_name': city_name,
            'current_conditions': current_conditions,
            'forecast': forecast
        }
        return render(request, 'weather/weather.html', context)
    return render(request, 'weather/weather.html', {'error': f'City {city_name} not found'})
