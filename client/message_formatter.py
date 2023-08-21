def rotate_long_message(message, message_max_length: int = 40):
    return message[1:] + message[0]

class MessageFormatter:
    def __init__(self, scroll_speed: float, req_line_length: int = 40):
        self.scroll_speed = scroll_speed
        self.req_line_length = req_line_length

    def enforce_line_length(self, line: str) -> str:
        if len(line) < self.req_line_length:
            line = line + (" " * (self.req_line_length - len(line)))
        return line[0:self.req_line_length]

    def format_line(self, line) -> bytearray:
        line_set_length = self.enforce_line_length(line)
        line_byte_array = bytearray()
        line_byte_array.extend(map(ord, line_set_length))
        return line_byte_array




