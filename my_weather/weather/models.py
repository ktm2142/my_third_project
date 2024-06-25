from django.db import models
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    accuweather_key = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}, ({self.country})"


class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    weather_text = models.CharField(max_length=100)
    icon_url = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.city.name} - {self.temperature}°C, {self.weather_text}"


class Forecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    day_icon_url = models.URLField()
    night_icon_url = models.URLField()
    day_phrase = models.CharField(max_length=100)
    night_phrase = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city.name} - {self.date}: {self.min_temperature}°C to {self.max_temperature}°C"


class CityImage(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image_url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return f"Image for {self.city.name}"


class SearchHistory(models.Model):
    query = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.query} - {self.timestamp}"
