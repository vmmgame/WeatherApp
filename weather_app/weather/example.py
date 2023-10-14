import datetime as dt 
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "6bbaa207747b294ca2a34dba5f5ed709"
CITY = "Chicago"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=inperial"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return round(celsius,2), round(fahrenheit,2)

responce = requests.get(url).json()


temp_kelvin = responce['main']['temp']
temp_celcius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = responce['main']['feels_like']
feels_like_celcius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)


print(f"C: {temp_celcius}     F: {temp_fahrenheit}")
print(f"Feels like C: {feels_like_celcius}     F: {feels_like_fahrenheit}")
print(responce)
print(type(responce))
print(type(temp_kelvin))