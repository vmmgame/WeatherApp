import requests

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .form import CityForm

# Create your views here.

user_city = ''

def home_page(request):
    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            global user_city
            user_city = form.cleaned_data['city']
            return HttpResponseRedirect('results')
    
    form = CityForm()
    
    return render(request, 'weather/home_page.html', {
        "form": form
    })


def results_page(request):
    response = get_weather_data(city=user_city)

    temp = round(response['main']['temp'], 0)
    feels_like = response.get('main', {}).get('feels_like')
    description = response['weather'][0]['description']

    return render(request, 'weather/results_page.html', {
        "temp": convert_to_f(temp),
        "feels_like": convert_to_f(feels_like),
        "descript": description,
        "city": user_city
    })


def get_weather_data(city):
    API_KEY = "6bbaa207747b294ca2a34dba5f5ed709"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=inperial"
    print("Get Weather: ", city)
    try:
        response = requests.get(url).json()
    except (requests.ConnectionError, requests.HTTPError):
        return Http404()
    return response
    


def convert_to_f(temp):
    return round((temp - 273.15) * (9/5) + 32,0)