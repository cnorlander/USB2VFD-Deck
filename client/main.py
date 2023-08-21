# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import serial
REQ_MESSAGE_LENGTH = 40
NC_MESSAGE = "DISCONNECTED"
GO_HOME = bytearray.fromhex("fe48")
GO_LINE_2 = bytearray.fromhex("fe470102")
MAX_FRAME_RATE = 1

def format_line(line: str):
    if len(line) < REQ_MESSAGE_LENGTH:
        line = line + (" " * (REQ_MESSAGE_LENGTH - len(line)))
    return line[0:REQ_MESSAGE_LENGTH]

def main():
    vfd_serial_conn = serial.Serial(
        port='COM5',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )


    count = 0

    while True:
        vfd_serial_conn.write(GO_HOME)
        message = "o8uY9f6D8a22DNOpdaGfbLQ " + str(count)
        message2 = "!@#$%^&*()_-+={}[]:;?/>" + str(count)
        count = count + 1
        line_1 = format_line(message)
        line_1_byte_array = bytearray()
        line_1_byte_array.extend(map(ord, format_line(line_1)))
        vfd_serial_conn.write(line_1_byte_array)

        vfd_serial_conn.write(GO_LINE_2)
        line_2 = format_line(message2)
        line_2_byte_array = bytearray()
        line_2_byte_array.extend(map(ord, format_line(line_2)))
        vfd_serial_conn.write(line_2_byte_array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
