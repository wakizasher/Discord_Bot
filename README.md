## Weather Discord Bot
A simple Discord bot that provides weather information for cities requested by users. The bot connects to the OpenWeatherMap API to fetch current weather data and displays it in Discord channels.

## Features
Get current weather data for any city through Discord
Display temperature, feels-like temperature, humidity, wind speed and short description
Simple command structure with $ prefix

## Requirements
Python 3.6+
discord.py library
requests library
OpenWeatherMap API key


## Invite the bot to your server:
Go to OAuth2 > URL Generator
Select "bot" scope and appropriate permissions (Send Messages, Read Messages/View Channels)
Copy and visit the generated URL to add the bot to your server



Usage
Run the bot:
`python discord_bot.py`
In your Discord server, use the command:
`$CityName`
For example: $London 
The bot will respond with current weather information for the specified city.

## Files
discord_bot.py: Main Discord bot file that handles messages and commands
weather.py: Module for interacting with the OpenWeatherMap API
weather.txt: Temporary file where weather data is stored
