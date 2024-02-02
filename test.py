from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from gpiozero import Button
from datetime import datetime, date
import requests  # Corrected import for requests

# Replace with your Google Sheet ID and JSON key file path
sheet_id = '1xnXJfhz5oLGKoT2hyJWT-4kWI0T1CIj0-TTeNxeKMFQ'
json_key_file = '/creds/service_account.json'
API_URL = "http://api.henriserverack.com/get_sheet_data"

# Specify GPIO pins for buttons and LEDs
button1_pin = 3  # Adjust pin numbers as needed
button2_pin = 27
button3_pin = 10

# Create Button objects
button1 = Button(button1_pin)
button2 = Button(button2_pin)
button3 = Button(button3_pin)

# Authenticate with Google Sheets API using google-auth
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(json_key_file, scopes=scope)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_key(sheet_id).sheet1

def make_api_request():
    response = requests.get(API_URL)  # Use requests for HTTP calls
    data = response.json()
    print(data)
    return data

# Function to add a row to the spreadsheet
def add_row(timestamp, action, name):
    worksheet.append_row([timestamp, action, name])

# Function to check if a person is currently clocked in
def is_clocked_in(name):
    api_data = make_api_request()  # Call the function
    # ... (rest of the function remains the same)

# Monitor button presses and handle clock in/out actions
while True:
    # ... (rest of the code remains the same)