import asyncio
import json

from env_canada import ECWeather

def get_current_weather(latitude: int, longitude: int) -> str:
    ec_en = ECWeather(coordinates=(latitude, longitude))
    asyncio.run(ec_en.update())
    condition = ec_en.conditions['condition']['value']
    if not condition:
        condition = ""

    weather_string = f"{condition} {ec_en.conditions['temperature']['value']}| HI:{ec_en.conditions['high_temp']['value']}|"
    return weather_string

