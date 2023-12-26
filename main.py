import requests
from datetime import datetime as dt
import os

APP_ID = "[SET VALUES]"
APP_KEY = "[SET VALUES]"
SHEETY_TOKEN = "[SET VALUES]"
SHEETY_API_ENDPOINT = "[SET VALUES]"

# API endpoints
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# set environment variables
os.environ["APP_ID"] = APP_ID
os.environ["APP_KEY"] = APP_KEY
os.environ["SHEETY_API_ENDPOINT"] = SHEETY_API_ENDPOINT
os.environ["SHEETY_TOKEN"] = SHEETY_TOKEN
os.environ["SHEETY_API_ENDPOINT"] = SHEETY_API_ENDPOINT

# set body stats
GENDER = "female"
WEIGHT = "55"
HEIGHT = "158"
AGE = "25"

# parameters and headers for API
parameters = {
    "query": input("What exercises did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id":APP_ID,
    "x-app-key": APP_KEY,
}

sheety_headers = {
    "Authorization": os.environ.get("SHEETY_TOKEN")
}

# get health data
response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
data = response.json()

# prepare data for sheety
date = dt.now().date()
date = date.strftime("%m-%d-%y")
time = dt.now().time()
time = time.strftime("%I:%M %p")

# store data into sheety
for exercise in data["exercises"]:
    sheety_parameters = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_API_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(response.text)





