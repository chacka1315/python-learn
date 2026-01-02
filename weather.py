import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_weather():
    location = input("Enter a city name: ")
    req_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/today?unitGroup=metric&key={os.getenv('API_KEY')}&contentType=json"
    print("URL: ", req_url)

    weather_data = requests.get(req_url).json()

    print("\n****************FORECAST******************\n\n")
    print(f"📍  Address: {weather_data['resolvedAddress']}\n".capitalize())
    print(f"🌍  Timezon: {weather_data['timezone']}\n")
    print(f"🌡️  Temperature: {weather_data['currentConditions']['temp']} °C\n")
    print(f"🌤️  Conditions: {weather_data['days'][0]['conditions']}\n")
    print(f"🌈  Description: {weather_data['days'][0]['description']}\n")
    print("\n****************FORECAST********************\n")
    # pprint(weather_data)


if __name__ == "__main__":
    get_weather()
