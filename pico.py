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
led1 = digitalio.DigitalInOut(board.GP28)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP27)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP26)
led3.direction = digitalio.Direction.OUTPUT
led4 = digitalio.DigitalInOut(board.GP22)
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.GP21)
led5.direction = digitalio.Direction.OUTPUT
led6 = digitalio.DigitalInOut(board.GP20)
led6.direction = digitalio.Direction.OUTPUT


def control_led(api_data):
    #data2 = json.loads(api_data)
    #print(api_data[0])
    #print(api_data["data"][0])
    #if api_data and api_data[0] == "Clocked In":
    clocked_in = api_data["data"]
    if api_data["data"][0] == "Clocked In":
        #print(api_data["data"][0])
        #print("om")
        # Turn on the LED
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

def make_api_request():
    response = requests.get(API_URL)
    #print(response)
    data = response.json()
    print(data)
    return data
    #if response.status_code == 200:
    #    data = response.json()
    #    return data
    #else:
    #    print("API request failed:", response.status_code)
    #    return None

def main():
    # Connect to Wi-Fi
    ##wlan = connect_wifi()
    #  connect to your SSID
    #print()
    #print("Connecting to WiFi")
    #wifi.radio.connect("southwest-wireless", "southwwifi000")
    #print("Connected to WiFi")
    #pool = socketpool.SocketPool(wifi.radio)
    #try:
    #    #connect_wifi()
    #    if wifi.radio.connected:
    #        print("Connected to WiFi!")
    #    else:
    #        print("WiFi connection failed")
    #        return
    #except Exception as e:
    #    print("Error connecting to WiFi:", e)
    #    return
    while True:
        try:
            # Make API request
            api_data = make_api_request()
            # Control LED based on API data
            control_led(api_data)

            # Wait for some time before the next request
            time.sleep(2)  # Adjust the delay as needed

        except Exception as e:
            #response = requests.get(url=API_URL)
            #print(response)
            #print("Error:", e)
            #print(api_data[1])
            print("lol")
            time.sleep(10)

if __name__ == "__main__":
    main()