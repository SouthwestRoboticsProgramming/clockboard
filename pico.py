import board
import adafruit_requests
import time
import digitalio

import wifi
import socketpool

print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect("southwest-wireless", "southwwifi000")

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

requests = adafruit_requests.Session(pool)

# Replace this with the URL of your API
API_URL = "http://api.henriserverack.com/get_sheet_data"

def define_led(pin):
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    return led

leds = [define_led(pin) for pin in [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
    board.GP18, board.GP19, board.GP20, board.GP21
]]

def make_api_request():
    response = requests.get(API_URL)
    data = response.json()
    print(data)
    return data

def control_leds(api_data):
    for i in range(len(leds)):
        clocked_in = (api_data["data"][i] == "Clocked In");
        leds[i].value = clocked_in

def main():
    while True:
        try:
            # Make API request
            api_data = make_api_request()
            # Control LEDs based on API data
            control_leds(api_data)

            # Wait for some time before the next request
            time.sleep(2)  # Adjust the delay as needed

        except Exception:
            print("lol")
            time.sleep(10)

if __name__ == "__main__":
    main()
