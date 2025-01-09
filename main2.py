import serial

port_name = "/dev/ttyUSB0"
port_baud = 115200

pico_serial = serial.Serial(port_name, port_baud)
pico_start_bit = 0b10000000

def send_leds_to_pico(led_states: list[bool]):
    led_data = [pico_start_bit, 0, 0, 0, 0]
    for i in range(len(led_states)):
        row = i % 5
        col = i // 5
        led_data[col] |= (1 << row)

    led_bytes = bytes(led_data)
    pico_serial.write(led_bytes)
    
while True:
    read_button()
    if button:
        toggle clockin api -> is clock in
        led set to clock in
        send led
