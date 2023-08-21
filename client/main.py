# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from vfd_service import SerialVFD
from message_formatter import MessageFormatter, rotate_long_message
import time
import pytz
import serial
from datetime import datetime, timezone
from zoneinfo import ZoneInfo







def main():
    vfd = SerialVFD('COM5')
    formatter = MessageFormatter(scroll_speed=0.1)
    local_timezone = pytz.timezone("America/Los_Angeles")
    line_1_message = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%^&*()_-+={}[]:;?/>|!@#$%^&*()_-+={}[]:;?/><|.,`~"



    while True:
        current_time = datetime.now(local_timezone)
        line_2_message = current_time.strftime("%I:%M:%S %p")

        line_1_byte_array = formatter.format_line(line_1_message)
        line_2_byte_array = formatter.format_line(line_2_message)
        vfd.push_frame(line_1_byte_array, line_2_byte_array)
        line_1_message = rotate_long_message(line_1_message)
        time.sleep(0.1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
