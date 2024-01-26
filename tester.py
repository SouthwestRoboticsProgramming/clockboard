import requests

response = requests.get('http://api.henriserverack.com/get_sheet_data')  # Replace with your API endpoint
data = response.json()
print(data['data'])  # This will print the values from cells J2 to J23
