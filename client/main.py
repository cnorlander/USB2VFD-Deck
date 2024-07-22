import os
from vfd_service import SerialVFD
from message_formatter import MessageFormatter, rotate_long_message
import time
import pytz
import serial
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
from weather import get_current_weather
from rss import get_top_posts

load_dotenv()


def main():
    vfd = SerialVFD('COM' + os.getenv("COMPORT_NUMBER"))
    formatter = MessageFormatter(scroll_speed=0.1)
    local_timezone = pytz.timezone(os.getenv("TIME_ZONE"))
    window_size = 40

    line_1_message = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%^&*()_-+={}[]:;?/>|!@#$%^&*()_-+={}[]:;?/><|.,`~"

    # Weather Setup
    weather_latitude = int(os.getenv("WEATHER_LATITUDE"))
    weather_longitude = int(os.getenv("WEATHER_LONGITUDE"))
    weather_update_time = None
    weather_string = ""

    # RSS setup
    rss_url = os.getenv("RSS_URL")
    rss_post_count = int(os.getenv("RSS_POST_COUNT"))
    rss_ticker_string = ""
    rss_update_time = None


    while True:
        current_time = datetime.now()

        # Fetch the weather every hour
        if not weather_update_time or current_time - weather_update_time > timedelta(minutes=10):
            weather_update_time = current_time
            weather_string = get_current_weather(weather_latitude, weather_longitude)
            line_2_message = weather_string

        # Fetch the news every hour (forms line 1)
        if not rss_update_time or current_time - rss_update_time > timedelta(minutes=10):
            rss_update_time = current_time
            line_1_message = get_top_posts(rss_url, rss_post_count)

        # Form line 2
        local_time = datetime.now(local_timezone)
        local_time_string = local_time.strftime('%I:%M:%S %p').strip("0")
        line_2_message = rotate_long_message(line_2_message, window_size - (len(local_time_string) + 1))


        # format the frames and display them
        line_1_byte_array = formatter.format_line(line_1_message)
        line_2_byte_array = formatter.format_line(line_2_message, end_overlay=local_time_string)
        vfd.push_frame(line_1_byte_array, line_2_byte_array)

        # Scroll speed for the message formatter not working yet. Adjust sleep as needed for scroll speed
        line_1_message = rotate_long_message(line_1_message)
        time.sleep(0.07)

if __name__ == '__main__':
    main()


