import serial
import time

def serial_connect(serial_port):
    serial_conn = None
    while True:
        exception_tossed = False
        try:
            serial_conn = serial.Serial(
                port=serial_port,
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
        except serial.serialutil.SerialException as e:
            exception_tossed = True
        if not exception_tossed:
            return serial_conn
        print("Connection Failed... Waiting to try again...")
        time.sleep(5)

class SerialVFD:
    GO_HOME = bytearray.fromhex("fe48")
    GO_LINE_2 = bytearray.fromhex("fe470102")
    MAX_FRAME_RATE = 10

    def __init__(self, serial_port, nc_message: str = "DISCONNECTED"):
        self.serial_port = serial_port
        self.serial_conn = serial_connect(serial_port)
        self.last_frame_time = time.time()
        self.nc_message = nc_message

    def push_frame(self, line_1_byte_array: bytearray, line_2_byte_array: bytearray):
        now = time.time()
        time_delta = now - self.last_frame_time
        self.last_frame_time = now
        frame_limit = 1.0 / SerialVFD.MAX_FRAME_RATE
        if time_delta >= frame_limit:
            try:
                self.serial_conn.write(SerialVFD.GO_HOME)
                self.serial_conn.write(line_1_byte_array)
                self.serial_conn.write(SerialVFD.GO_LINE_2)
                self.serial_conn.write(line_2_byte_array)
            except serial.serialutil.SerialException as e:
                self.serial_conn = serial_connect(self.serial_port)


if __name__ == '__main__':
    print("Testing VFD Service")
    vfd = SerialVFD(serial_port='COM5')
    print("Test Complete!")



