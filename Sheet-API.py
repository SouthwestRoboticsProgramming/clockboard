##to start api service: gunicorn -b 127.0.0.1:5132 -w 4 sheet_api:app --daemon

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, jsonify
app = Flask(__name__)

# Authentication setup
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
gc = gspread.authorize(credentials)

# Open the spreadsheet
sheet = gc.open_by_key('1u2M_qIo_XLVv5HPKYmyX_ehruxVFECf8vmXNKnErk4U')  # Replace with your spreadsheet's key
worksheet = sheet.worksheet('Data')

# Define the API endpoint
@app.route('/get_sheet_data') 
def get_sheet_data():
    values = worksheet.range('J2:J23')  # Fetch values from cells J2 to J23
    data = [cell.value for cell in values]  # Extract values into a list
    return jsonify({'data': data})  # Return the data as JSON
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)