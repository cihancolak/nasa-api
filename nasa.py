import requests
from datetime import datetime
date_format = "%Y/%m/%d"

API_KEY =  "4z6ePBjtbBLWc8CLi9S5nrWlKBun1KmEatSUxQt9" 
BASE_URL = "https://api.nasa.gov/DONKI/RBE/"

startdate = input("Enter Start Date?\n(Enter Start Date as \"yyyy-MM-dd\")\n-> ")
enddate = input("Enter End Date?\n(Enter End Date as \"yyyy-MM-dd\")\n-> ")
request_url = f"{BASE_URL}?startDate={startdate}&endDate={enddate}&api_key={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred")
