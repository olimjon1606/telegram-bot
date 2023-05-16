import telegram
from telegram.ext import Updater, CommandHandler
import requests

# Set up the Telegram bot token and weather API key
bot_token = 'YOUR_BOT_TOKEN'
weather_api_key = 'YOUR_WEATHER_API_KEY'

# Create an instance of the Telegram bot
bot = telegram.Bot(token=bot_token)

# Define the function to handle the /weather command
def weather(update, context):
    # Get the chat ID and the location from the user's message
    chat_id = update.message.chat_id
    location = ' '.join(context.args)

    # Send a request to the weather API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}'
    response = requests.get(url)
    data = response.json()

    # Extract the relevant weather information from the response
    if data['cod'] == 200:
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Format the weather information into a message
        message = f'Weather in {location}:\n\n' \
                  f'Description: {weather_desc}\n' \
                  f'Temperature: {temp} K\n' \
                  f'Humidity: {humidity}%\n' \
                  f'Wind Speed: {wind_speed} m/s'
    else:
        message = f'Error retrieving weather information for {location}.'

    # Send the weather information as a reply to the user
    bot.send_message(chat_id=chat_id, text=message)

# Set up the Telegram bot updater and dispatcher
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Add the weather command handler
dispatcher.add_handler(CommandHandler('weather', weather))

# Start the bot
updater.start_polling()
