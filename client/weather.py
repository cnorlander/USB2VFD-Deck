import asyncio
import json

from env_canada import ECWeather

def get_current_weather() -> str:
    ec_en = ECWeather(coordinates=(49, -122))
    asyncio.run(ec_en.update())
    weather_string = f"{ec_en.conditions['condition']['value']} {ec_en.conditions['temperature']['value']}| HI:{ec_en.conditions['high_temp']['value']}|"
    return weather_string

