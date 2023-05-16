import requests
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
    except Exception as ex:
        print(ex)
        print("Please check city name!")

def main():
    city = input("Enter City: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()