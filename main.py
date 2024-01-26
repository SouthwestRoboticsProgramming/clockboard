from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gpiozero  import Button, LED
from datetime import datetime, date


# Replace with your Google Sheet ID and JSON key file path
sheet_id = 'YOUR_SHEET_ID'
json_key_file = '/path/to/credentials.json'

# Specify GPIO pins for buttons and LEDs
button1_pin = 17  # Adjust pin numbers as needed
button2_pin = 27
button3_pin = 22

# Create Button and LED objects
button1 = Button(button1_pin)
button2 = Button(button2_pin)
button3 = Button(button3_pin)

# Authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key_file, scope)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_key(sheet_id).sheet1

# Function to add a row to the spreadsheet
def add_row(timestamp, action, name):
    worksheet.append_row([timestamp, action, name])

# Function to check if a person is currently clocked in
def is_clocked_in(name):
    today = date.today().strftime("%Y-%m-%d")
    for row in worksheet.get_all_values():
        if row[2] == name and row[0].startswith(today) and row[1] == "clock in":
            return True
    return False

# Monitor button presses and handle clock in/out actions
while True:
    if button1.is_pressed:
        action = "clock out" if is_clocked_in("Henri") else "clock in"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Henri")
        led1.value = action == "clock in"  # Turn LED on for "clock in", off for "clock out"
    elif button2.is_pressed:
        action = "clock out" if is_clocked_in("Clark") else "clock in"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Clark")
        led2.value = action == "clock in"
    elif button3.is_pressed:
        action = "clock out" if is_clocked_in("Anders") else "clock in"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Anders")
        led3.value = action == "clock in"

