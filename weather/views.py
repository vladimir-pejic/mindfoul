from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.views.generic import DeleteView
from .models import City
from .forms import CityForm
import requests


@login_required()
def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + settings.WEATHER_API

    # validate if the city can be found on weather API
    if request.method == 'POST':
        check_city = requests.get(url.format(request.POST['name'])).json()
        if 'weather' in check_city:
            form = CityForm(request.POST)
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
        else:
            messages.error(request, f'The city cannot be found!')
            return redirect('weather')

    # Continue with loading all cities (event the one just saved, if saved) and show them
    cities = City.objects.filter(author=request.user)
    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()
        if 'main' in city_weather:
            weather = {
                'city': city.name,
                'city_id': city.id,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)


class CityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = City
    success_url = '/weather/'

    def test_func(self):
        city = self.get_object()
        if self.request.user == city.author:
            return True
        return False
