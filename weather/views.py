from django.shortcuts import render
from django.conf import settings
from .models import City
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + settings.WEATHER_API
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()
        print(city)
        print(city_weather)
        if 'main' in city_weather:
            weather = {
                'city': city.name,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)

    context = {'weather_data': weather_data}

    return render(request, 'weather/index.html', context)
