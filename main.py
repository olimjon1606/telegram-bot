import requests
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        print(data)
    except Exception as ex:
        print(ex)
        print("Please check city name!")

def main():
    city = input("Enter City: ")
    get_weather(city, open_weather_token)

if __name__ = '__main__':
    main()