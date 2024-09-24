from google.oauth2.service_account import Credentials
import gspread
from gpiozero import Button
from datetime import datetime
import requests  # Typo corrected from "urequets"
print("Loaded modules")


# Replace with your Google Sheet ID and JSON key file path
sheet_id = '1u2M_qIo_XLVv5HPKYmyX_ehruxVFECf8vmXNKnErk4U'
json_key_file = '/creds/service_account.json'
API_URL = "http://api.henriserverack.com/get_sheet_data"

# Authenticate with Google Sheets API using google-auth
SCOPES = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(json_key_file, scopes=SCOPES)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_key(sheet_id).sheet1
print("Loaded credentials")


def make_api_request():
    response = requests.get(API_URL)  # Use authorized session
    data = response.json()
    return data

def add_row(timestamp, action, name):
    worksheet.append_row([timestamp, action, name], value_input_option='USER_ENTERED')

def button_pressed(api_id, name):
    global api_data
    clocked_in = (api_data["data"][api_id] == "Clocked In")
    
    action = "Clock Out" if clocked_in else "Clock In"
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    add_row(timestamp, action, name)

    # Logging
    print(f"[{timestamp}] {action}: {name}")

def define_button(api_id, pin, name):
    # TODO: Do these need debouncing? Default is to not debounce at all
    button = Button(pin)
    button.when_pressed = lambda: button_pressed(api_id, name)


# Get initial data
api_data = make_api_request()

# api_id, pin, name
define_button( 0,  2, "Mason")
define_button( 1,  3, "Cameron")
define_button( 2,  4, "Jonah")
define_button( 3, 17, "Jerry")
define_button( 4, 27, "Henri "),
define_button( 5, 22, "Liam")
define_button( 6, 10, "Ki Ba"),
define_button( 7,  9, "Oliver")
define_button( 8, 11, "Clark")
define_button( 9,  5, "Rain")
define_button(10,  6, "Malcom")
define_button(11, 13, "Henry "),
define_button(12, 19, "Auggie")
define_button(13, 26, "Anders")
define_button(14, 14, "Victor")
define_button(15, 15, "Finn")
define_button(16, 18, "Sam")
define_button(17, 23, "Neah")
define_button(18, 24, "Sophia")
define_button(19, 25, "Eddie")
define_button(20,  8, "Sadie")
define_button(21,  7, "Alena")

# Continuously update data from API
while True:
    api_data = make_api_request()
    # TODO: Do we want to sleep for some time to not be annoying to the server?
