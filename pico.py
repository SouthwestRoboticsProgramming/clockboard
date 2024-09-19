import board
import adafruit_requests
import time
import digitalio
import json

import os
import ipaddress
import wifi
import socketpool

print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect("southwest-wireless", "southwwifi000")

#print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

requests = adafruit_requests.Session(pool)

# Replace this with the URL of your API
API_URL = "http://api.henriserverack.com/get_sheet_data"

#headers = {"user-agent": "blinka/1.0.0"}
# Replace this with the GPIO pin number where your LED is connected
led1 = digitalio.DigitalInOut(board.GP0)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP1)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP2)
led3.direction = digitalio.Direction.OUTPUT
led4 = digitalio.DigitalInOut(board.GP3)
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.GP4)
led5.direction = digitalio.Direction.OUTPUT
led6 = digitalio.DigitalInOut(board.GP5)
led6.direction = digitalio.Direction.OUTPUT
led7 = digitalio.DigitalInOut(board.GP6)
led7.direction = digitalio.Direction.OUTPUT
led8 = digitalio.DigitalInOut(board.GP7)
led8.direction = digitalio.Direction.OUTPUT
led9 = digitalio.DigitalInOut(board.GP8)
led9.direction = digitalio.Direction.OUTPUT
led10 = digitalio.DigitalInOut(board.GP9)
led10.direction = digitalio.Direction.OUTPUT
led11 = digitalio.DigitalInOut(board.GP10)
led11.direction = digitalio.Direction.OUTPUT
led12 = digitalio.DigitalInOut(board.GP11)
led12.direction = digitalio.Direction.OUTPUT
led13 = digitalio.DigitalInOut(board.GP12)
led13.direction = digitalio.Direction.OUTPUT
led14 = digitalio.DigitalInOut(board.GP13)
led14.direction = digitalio.Direction.OUTPUT
led15 = digitalio.DigitalInOut(board.GP14)
led15.direction = digitalio.Direction.OUTPUT
led16 = digitalio.DigitalInOut(board.GP15)
led16.direction = digitalio.Direction.OUTPUT
led17 = digitalio.DigitalInOut(board.GP16)
led17.direction = digitalio.Direction.OUTPUT
led18 = digitalio.DigitalInOut(board.GP17)
led18.direction = digitalio.Direction.OUTPUT
led19 = digitalio.DigitalInOut(board.GP18)
led19.direction = digitalio.Direction.OUTPUT
led20 = digitalio.DigitalInOut(board.GP19)
led20.direction = digitalio.Direction.OUTPUT
led21 = digitalio.DigitalInOut(board.GP20)
led21.direction = digitalio.Direction.OUTPUT
led22 = digitalio.DigitalInOut(board.GP21)
led22.direction = digitalio.Direction.OUTPUT


def control_led(api_data):
    clocked_in = api_data["data"]
    if api_data["data"][0] == "Clocked In":
        led1.value = True
    if api_data["data"][0] == "Not Clocked In":
        led1.value = False
    if api_data["data"][1] == "Clocked In":
        led2.value = True
    if api_data["data"][1] == "Not Clocked In":
        led2.value = False
    if api_data["data"][2] == "Clocked In":
        led3.value = True
    if api_data["data"][2] == "Not Clocked In":
        led3.value = False
    if api_data["data"][3] == "Clocked In":
        led4.value = True
    if api_data["data"][3] == "Not Clocked In":
        led4.value = False
    if api_data["data"][4] == "Clocked In":
        led5.value = True
    if api_data["data"][4] == "Not Clocked In":
        led5.value = False
    if api_data["data"][5] == "Clocked In":
        led6.value = True
    if api_data["data"][5] == "Not Clocked In":
        led6.value = False
    if api_data["data"][6] == "Clocked In":
        led7.value = True
    if api_data["data"][6] == "Not Clocked In":
        led7.value = False
    if api_data["data"][7] == "Clocked In":
        led8.value = True
    if api_data["data"][7] == "Not Clocked In":
        led8.value = False
    if api_data["data"][8] == "Clocked In":
        led9.value = True
    if api_data["data"][8] == "Not Clocked In":
        led9.value = False
    if api_data["data"][9] == "Clocked In":
        led10.value = True
    if api_data["data"][9] == "Not Clocked In":
        led10.value = False
    if api_data["data"][10] == "Clocked In":
        led11.value = True
    if api_data["data"][10] == "Not Clocked In":
        led11.value = False
    if api_data["data"][11] == "Clocked In":
        led12.value = True
    if api_data["data"][11] == "Not Clocked In":
        led12.value = False
    if api_data["data"][12] == "Clocked In":
        led13.value = True
    if api_data["data"][12] == "Not Clocked In":
        led13.value = False
    if api_data["data"][13] == "Clocked In":
        led14.value = True
    if api_data["data"][13] == "Not Clocked In":
        led14.value = False
    if api_data["data"][14] == "Clocked In":
        led15.value = True
    if api_data["data"][14] == "Not Clocked In":
        led15.value = False
    if api_data["data"][15] == "Clocked In":
        led16.value = True
    if api_data["data"][15] == "Not Clocked In":
        led16.value = False
    if api_data["data"][16] == "Clocked In":
        led17.value = True
    if api_data["data"][16] == "Not Clocked In":
        led17.value = False
    if api_data["data"][17] == "Clocked In":
        led18.value = True
    if api_data["data"][17] == "Not Clocked In":
        led18.value = False
    if api_data["data"][18] == "Clocked In":
        led19.value = True
    if api_data["data"][18] == "Not Clocked In":
        led19.value = False
    if api_data["data"][19] == "Clocked In":
        led20.value = True
    if api_data["data"][19] == "Not Clocked In":
        led20.value = False
    if api_data["data"][20] == "Clocked In":
        led21.value = True
    if api_data["data"][20] == "Not Clocked In":
        led21.value = False
    if api_data["data"][21] == "Clocked In":
        led22.value = True
    if api_data["data"][21] == "Not Clocked In":
        led22.value = False




def make_api_request():
    response = requests.get(API_URL)
    #print(response)
    data = response.json()
    print(data)
    return data

def main():
    while True:
        try:
            # Make API request
            api_data = make_api_request()
            # Control LED based on API data
            control_led(api_data)

            # Wait for some time before the next request
            time.sleep(2)  # Adjust the delay as needed

        except Exception as e:
            print("lol")
            time.sleep(10)

if __name__ == "__main__":
    main()