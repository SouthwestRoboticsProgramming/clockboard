import time
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession
import gspread
from gpiozero import Button
from datetime import datetime, date
import requests  # Typo corrected from "urequets"

print("Loaded modules")
# Replace with your Google Sheet ID and JSON key file path
sheet_id = '1xnXJfhz5oLGKoT2hyJWT-4kWI0T1CIj0-TTeNxeKMFQ'
json_key_file = '/creds/service_account.json'
API_URL = "http://api.henriserverack.com/get_sheet_data"

print("Loaded credentials")
# Specify GPIO pins for buttons and LEDs

##set 1 (left?)
button1_pin = 2  # Adjust pin numbers as needed
button2_pin = 3
button3_pin = 4
button4_pin = 17
button5_pin = 27
button6_pin = 22
button7_pin = 10
button8_pin = 9
button9_pin = 11
button10_pin = 5
button11_pin = 6
button12_pin = 13
button13_pin = 19
button14_pin = 26

##set 2 (right?)
button15_pin = 14
button16_pin = 15
button17_pin = 18
button18_pin = 23
button19_pin = 24
button20_pin = 25
button21_pin = 8
button22_pin = 7




# Create Button objects
button1 = Button(button1_pin)
button2 = Button(button2_pin)
button3 = Button(button3_pin)
button4 = Button(button4_pin)
button5 = Button(button5_pin)
button6 = Button(button6_pin)
button7 = Button(button7_pin)
button8 = Button(button8_pin)
button9 = Button(button9_pin)
button10 = Button(button10_pin)
button11 = Button(button11_pin)
button12 = Button(button12_pin)
button13 = Button(button13_pin)
button14 = Button(button14_pin)
button15 = Button(button15_pin)
button16 = Button(button16_pin)
button17 = Button(button17_pin)
button18 = Button(button18_pin)
button19 = Button(button19_pin)
button20 = Button(button20_pin)
button21 = Button(button21_pin)
button22 = Button(button22_pin)


# Authenticate with Google Sheets API using google-auth
SCOPES = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(json_key_file, scopes=SCOPES)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_key(sheet_id).sheet1

def make_api_request():
    response = requests.get(API_URL)  # Use authorized session
    data = response.json()
    return data

# Function to add a row to the spreadsheet
def add_row(timestamp, action, name):
    worksheet.append_row([timestamp, action, name], value_input_option='USER_ENTERED')

# Function to check if a person is currently clocked in
def is_clocked_in(name):
    api_data = make_api_request()
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
    if name == "Jerry":
        if api_data["data"][3] == "Clocked In":
            return True
        if api_data["data"][3] == "Not Clocked In":
            return False
    if name == "Henri K":
        if api_data["data"][4] == "Clocked In":
            return True
        if api_data["data"][4] == "Not Clocked In":
            return False
    if name == "Nathan":
        if api_data["data"][5] == "Clocked In":
            return True
        if api_data["data"][5] == "Not Clocked In":
            return False
    if name == "Ki Bae":
        if api_data["data"][6] == "Clocked In":
            return True
        if api_data["data"][6] == "Not Clocked In":
            return False
    if name == "Lael":
        if api_data["data"][7] == "Clocked In":
            return True
        if api_data["data"][7] == "Not Clocked In":
            return False
    if name == "Clark":
        if api_data["data"][8] == "Clocked In":
            return True
        if api_data["data"][8] == "Not Clocked In":
            return False
    if name == "Ryan":
        if api_data["data"][9] == "Clocked In":
            return True
        if api_data["data"][9] == "Not Clocked In":
            return False
    if name == "Will":
        if api_data["data"][10] == "Clocked In":
            return True
        if api_data["data"][10] == "Not Clocked In":
            return False
    if name == "Henry N":
        if api_data["data"][11] == "Clocked In":
            return True
        if api_data["data"][11] == "Not Clocked In":
            return False
    if name == "Haley":
        if api_data["data"][12] == "Clocked In":
            return True
        if api_data["data"][12] == "Not Clocked In":
            return False
    if name == "Anders":
        if api_data["data"][13] == "Clocked In":
            return True
        if api_data["data"][13] == "Not Clocked In":
            return False
    if name == "Victor":
        if api_data["data"][14] == "Clocked In":
            return True
        if api_data["data"][14] == "Not Clocked In":
            return False
    if name == "Finn":
        if api_data["data"][15] == "Clocked In":
            return True
        if api_data["data"][15] == "Not Clocked In":
            return False
    if name == "Sam":
        if api_data["data"][16] == "Clocked In":
            return True
        if api_data["data"][16] == "Not Clocked In":
            return False
    if name == "Leah":
        if api_data["data"][17] == "Clocked In":
            return True
        if api_data["data"][17] == "Not Clocked In":
            return False
    if name == "Dash":
        if api_data["data"][18] == "Clocked In":
            return True
        if api_data["data"][18] == "Not Clocked In":
            return False
    if name == "Eddie":
        if api_data["data"][19] == "Clocked In":
            return True
        if api_data["data"][19] == "Not Clocked In":
            return False
    if name == "Shepard":
        if api_data["data"][20] == "Clocked In":
            return True
        if api_data["data"][20] == "Not Clocked In":
            return False
    if name == "Alena":
        if api_data["data"][21] == "Clocked In":
            return True
        if api_data["data"][21] == "Not Clocked In":
            return False

while True:
    if button1.is_pressed:
        action = "Clock Out" if is_clocked_in("Mason") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Mason")
    if button2.is_pressed:
        action = "Clock Out" if is_clocked_in("Cameron") else "Clock In"
        add_row(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), action, "Cameron")
    if button3.is_pressed:
        action = "Clock Out" if is_clocked_in("Jack") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Jack")
    if button4.is_pressed:
        action = "Clock Out" if is_clocked_in("Jerry") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Jerry")
    if button5.is_pressed:
        action = "Clock Out" if is_clocked_in("Henri K") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Henri K")
    if button6.is_pressed:
        action = "Clock Out" if is_clocked_in("Nathan") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Nathan")
    if button7.is_pressed:
        action = "Clock Out" if is_clocked_in("Ki Bae") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Ki Bae")
    if button8.is_pressed:
        action = "Clock Out" if is_clocked_in("Lael") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Lael")
    if button9.is_pressed:
        action = "Clock Out" if is_clocked_in("Clark") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Clark")
    if button10.is_pressed:
        action = "Clock Out" if is_clocked_in("Ryan") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Ryan")
    if button11.is_pressed:
        action = "Clock Out" if is_clocked_in("Will") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Will")
    if button12.is_pressed:
        action = "Clock Out" if is_clocked_in("Henry N") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Henry N")
    if button13.is_pressed:
        action = "Clock Out" if is_clocked_in("Haley") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Haley")
    if button14.is_pressed:
        action = "Clock Out" if is_clocked_in("Anders") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Anders")
    if button15.is_pressed:
        action = "Clock Out" if is_clocked_in("Victor") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Victor")
    if button16.is_pressed:
        action = "Clock Out" if is_clocked_in("Finn") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Finn")
    if button17.is_pressed:
        action = "Clock Out" if is_clocked_in("Sam") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Sam")
    if button18.is_pressed:
        action = "Clock Out" if is_clocked_in("Leah") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Leah")
    if button19.is_pressed:
        action = "Clock Out" if is_clocked_in("Dash") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Dash")
        print("dash")
    if button20.is_pressed:
        action = "Clock Out" if is_clocked_in("Eddie") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Eddie")
    if button21.is_pressed:
        action = "Clock Out" if is_clocked_in("Shepard") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Shepard")
    if button22.is_pressed:
        action = "Clock Out" if is_clocked_in("Alena") else "Clock In"
        add_row(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, "Alena")
