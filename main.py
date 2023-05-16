import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"

    }


    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
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
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"https://source.unsplash.com/1600x900/?nature,rain"
              f"********* {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}  ********\n"
              f"Weather in City: {city}\nTemperature: {cur_weather}°C {wd}\n"
              f"Humidity: {humidity}\nPressure: {pressure}\nWind: {wind} m/s\n"
              f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of the Day: {length_of_the_day}\n"
              f"Have Great Day!!!")


    except Exception as ex:
        print(ex)
        print("Please check city name!")

def main():
    city = input("Enter City: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()