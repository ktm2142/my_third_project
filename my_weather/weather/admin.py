from django.contrib import admin

from .models import SearchHistory, WeatherData, City, Forecast, CityImage


admin.site.register(SearchHistory)
admin.site.register(WeatherData)
admin.site.register(City)
admin.site.register(Forecast)
admin.site.register(CityImage)
