import requests
import datetime as dt
from secret import APP_ID, NUTRITIONINX_API_KEY, SHEETY_TOKEN, SHEETY_ENDPOINT

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITIONINX_API_KEY,
}

exercise_params = {
    "query": input("Describe what you did today: "),
}

today = dt.datetime.today()
date = today.strftime(format="%d/%m/%Y")
time = today.strftime(format="%H:%M:%S")

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)

exercise_data = response.json()["exercises"][0]

sheety_header = {
    'Authorization': SHEETY_TOKEN
}
google_sheet_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_data["name"].title(),
        "duration": exercise_data["duration_min"],
        "calories": exercise_data["nf_calories"],
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=google_sheet_data, headers=sheety_header)
print(sheety_response.text)

