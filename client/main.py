# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from vfd_service import SerialVFD
from message_formatter import MessageFormatter, rotate_long_message
import time
import pytz
import serial
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
from weather import get_current_weather
from news import get_top_posts

load_dotenv()


def main():
    vfd = SerialVFD('COM' + os.getenv("COMPORT_NUMBER"))
    formatter = MessageFormatter(scroll_speed=0.1)
    local_timezone = pytz.timezone(os.getenv("TIME_ZONE"))
    rss_url = os.getenv("RSS_URL")
    line_1_message = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%^&*()_-+={}[]:;?/>|!@#$%^&*()_-+={}[]:;?/><|.,`~"
    last_weather_update = None
    weather_string = ""
    news_string = ""
    last_news_update = None


    while True:
        current_time = datetime.now()

        # Fetch the weather every hour
        if not last_weather_update or current_time - last_weather_update > timedelta(hours=1):
            last_weather_update = current_time
            weather_string = get_current_weather()

        # Fetch the news every hour (forms line 1)
        if not last_news_update or current_time - last_news_update > timedelta(hours=1):
            last_news_update = current_time
            line_1_message = get_top_posts(rss_url)

        # Form line 2
        local_time = datetime.now(local_timezone)
        line_2_message = local_time.strftime("%I:%M:%S %p") + "  " + weather_string

        # format the frames and display them
        line_1_byte_array = formatter.format_line(line_1_message)
        line_2_byte_array = formatter.format_line(line_2_message)
        vfd.push_frame(line_1_byte_array, line_2_byte_array)

        # Scroll speed for the message formatter not working yet. Adjust sleep as needed for scroll speed
        line_1_message = rotate_long_message(line_1_message)
        time.sleep(0.07)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
