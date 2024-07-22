import re
from unidecode import unidecode

def rotate_long_message(message, message_max_length: int = 40):
    if len(message) > message_max_length:
        return message[1:] + message[0]
    return message

def replace_offending_characters(input_string: str, placeholder_char='#') -> str:
    strict_alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%^&*()_-+={}[]:;?/>|!@#$%^&*()_-+={}[]:;?/><|.,`~'\""

    # Transliterate to ASCII using unidecode
    input_string = unidecode(input_string)

    # Create a set for fast lookup
    allowed_set = set(strict_alphabet)

    # Replace offending characters with the placeholder
    result = ''.join(char if char in allowed_set else placeholder_char for char in input_string)

    return result

def write_over_line_end(enforced_length_line, text):
    text = " " + text
    return enforced_length_line[0:len(enforced_length_line) - len(text)] + text

class MessageFormatter:
    def __init__(self, scroll_speed: float, req_line_length: int = 40):
        self.scroll_speed = scroll_speed
        self.req_line_length = req_line_length

    def enforce_line_length(self, line: str) -> str:
        if len(line) < self.req_line_length:
            line = line + (" " * (self.req_line_length - len(line)))
        return line[0:self.req_line_length]

    def format_line(self, line: str, end_overlay: str = None) -> bytearray:
        line = replace_offending_characters(line)
        line_set_length = self.enforce_line_length(line)
        if end_overlay:
            line_set_length = write_over_line_end(line_set_length, end_overlay)
        line_byte_array = bytearray()
        line_byte_array.extend(map(ord, line_set_length))
        return line_byte_array





