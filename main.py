from time import sleep
import gspread
from oauth2client.service_account import ServiceAccaountCredentials
from gpiozero  import Button
from datetime import datetime, date
import urequets



# Replace with your Google Sheet ID and JSON key file path
sheet_id = '1xnXJfhz5oLGKoT2hyJWT-4kWI0T1CIj0-TTeNxeKMFQ'
json_key_file = '/creds/service_account.json'
API_URL = "http://api.henriserverack.com/get_sheet_data"

# Specify GPIO pins for buttons and LEDs
button1_pin = 3  # Adjust pin numbers as needed
button2_pin = 27
button3_pin = 10

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

def make_api_request():
    response = urequests.get(API_URL)
    #print(response)
    data = response.json()
    print(data)
    return data

# Function to add a row to the spreadsheet
def add_row(timestamp, action, name):
    worksheet.append_row([timestamp, action, name])

# Function to check if a person is currently clocked in
def is_clocked_in(name):
    api_data = make_api_request
    if name == "Mason":
        if api_data["data"][0] == "Clocked In":
            return True
        if api_data["data"][0] == "Not Clocked In":
            return False
    if name == "Cameron":
        if api_data["data"][1] == "Clocked In":
            return True
        if api_data["data"][1] == "Not Clocked In":
            return False
    if name == "Jack":
        if api_data["data"][2] == "Clocked In":
            return True
        if api_data["data"][2] == "Not Clocked In":
            return False
        

# Monitor button presses and handle clock in/out actions
while True:
    if button1.is_pressed:
        action = "Clock Out" if is_clocked_in("Mason") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Mason")
    elif button2.is_pressed:
        action = "Clock out" if is_clocked_in("Cameron") else "Clock in"
        add_row(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), action, "Cameron")
    elif button3.is_pressed:
        action = "Clock out" if is_clocked_in("Jack") else "Clock in"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Jack")

