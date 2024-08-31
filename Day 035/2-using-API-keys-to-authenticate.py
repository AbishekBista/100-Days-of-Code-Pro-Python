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



