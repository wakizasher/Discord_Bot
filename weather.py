import datetime as dt
import requests
import creds_weather

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
file = 'weather.txt'

def get_weather_data(city_name:str):
    url = BASE_URL + "&q=" + city_name + "&units=metric" + "&APPID=" + creds_weather.weather_api


    response = requests.get(url).json()


    temp_celsius = response['main']['temp']
    feels_like_celsius = response['main']['feels_like']
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']


    # print(f"Temperature in {CITY}: {temp_celsius:.2f} C")
    # print(f"Temperature feels like: {feels_like_celsius} C")
    # print(f"Humidity is {humidity}%")
    # print(f"Wind speed is {humidity}%")

    with open(file, 'w+') as write_file:
        write_file.write(f"Temperature in {city_name}: {temp_celsius:.2f} C\n")
        write_file.write(f"Temperature feels like: {feels_like_celsius} C\n")
        write_file.write(f"Humidity is {humidity}%\n")
        write_file.write(f"Wind speed is {wind_speed}%\n")
        write_file.write(f"{description}")


    return file



