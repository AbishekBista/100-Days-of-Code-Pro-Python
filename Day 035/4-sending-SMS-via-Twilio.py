# bcd388dba5ae1fd82d622d631f2cff83
# 3b70d09bec54f8b555452513fd4be001
import requests
from twilio.rest import Client
from secret import MY_LAT, MY_LONG, api_key, account_sid, auth_token, recipient, sender



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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain. Carry an umbrella.",
    from_=sender,
    to=recipient
    )

    print(message.status)
 


