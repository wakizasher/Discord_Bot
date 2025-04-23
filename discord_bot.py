import discord
import requests
import json
import weather
import creds_discord

def get_weather(city_name):
    weather_file = weather.get_weather_data(city_name)

    with open(weather_file, 'r') as file:
        weather_file = file.read()
    return weather_file

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$'):
            city_name = message.content[1:].strip()

            # Get weather data:
            try:
                weather_info = get_weather(city_name)
                await message.channel.send(weather_info)
            except Exception as e:
                await message.send(f"Error getting weather: {str(e)}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(creds_discord.discord_api)