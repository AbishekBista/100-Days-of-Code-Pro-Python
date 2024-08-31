
import requests
from secret import MY_LAT, MY_LONG, api_key

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

print(weather_data)

first_twelve_hours = weather_data['hourly'][0:12]

condition_codes = [item['weather'][0]['id'] for item in first_twelve_hours ]

is_rainy = True in (condition_id < 700 for condition_id in condition_codes)

if is_rainy:
    print("Bring umbrella ☔")
else:
    print("Don't bring an umbrella")


