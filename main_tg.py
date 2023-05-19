import requests
import datetime
import random
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keep_alive import keep_alive

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
keep_alive()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
  await message.reply("Enter City name: ")


@dp.message_handler()
async def get_weather(message: types.Message):
  code_to_smile = {
    "Clear": "Clear \U00002600",
    "Clouds": "Cloudy \U00002601",
    "Rain": "Rain \U00002614",
    "Drizzle": "Drizzle \U00002614",
    "Thunderstorm": "Thunderstorm \U000026A1",
    "Snow": "Snow \U0001F328",
    "Mist": "Mist \U0001F32B"
  }

  try:
    r = requests.get(
      f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
    )
    data = r.json()

    city = data["name"]
    cur_weather = data["main"]["temp"]

    weather_desciption = data["weather"][0]["main"]
    if weather_desciption in code_to_smile:
      wd = code_to_smile[weather_desciption]
    else:
      wd = "Check outside yourself I don't know what weather it is!"
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    length_of_the_day = datetime.datetime.fromtimestamp(
      data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
        data["sys"]["sunrise"])

    random_number = random.randint(1, 9999)

    photo_url = f'https://source.unsplash.com/500x400/?{city},{wd}?random={random_number}'

    caption_text = (
      f"Weather in City:  {city}\nTemperature: {cur_weather}°C {wd}\n"
      f"Humidity: {humidity}\nPressure: {pressure}\nWind: {wind} m/s\n"
      f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of the Day: {length_of_the_day}\n"
      f"Have Great Day!!!")

    # Send photo with caption
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo_url,
                         caption=caption_text)

  except:
    await message.reply("\U00002620 Please check city name! \U00002620")


if __name__ == '__main__':
  executor.start_polling(dp)