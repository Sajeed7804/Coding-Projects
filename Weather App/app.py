import datetime as dt
import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "effe5e12eab2fa1c39a7e51342d33acf"
city = "Chittagong"

def kelvin_to_celcius_farenheit(kelvin):
    celcius = kelvin - 273.15
    farenheit = celcius * (9/5) + 32
    return celcius, farenheit

url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
 
temp_celcius, temp_farenheit = kelvin_to_celcius_farenheit(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']

feels_like_celcius, feels_like_farenheit = kelvin_to_celcius_farenheit(feels_like_kelvin)

humidity = response['main']['humidity']

description = response['weather'][0]['description']

wind_speed = response['wind']['speed']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {city}: {temp_celcius:.2f}°C or {temp_farenheit:.2f}°F")
print(f"Temperature in {city} feels like: {feels_like_celcius:.2f}°C or {feels_like_farenheit:.2f}°F")
print(f"Humidity in {city}: {humidity}%")
print(f"Wind speed in {city}: {wind_speed}m/s")
print(f"Generel weather in {city}: {description}")
print(f"Sunrise in {city}: {sunrise_time} local time")
print(f"Sunset in {city}: {sunset_time} local time")