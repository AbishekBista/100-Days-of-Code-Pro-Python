import requests
from secret import MY_LAT, MY_LONG
import datetime as dt
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0&tzid=Asia/Kathmandu")
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = dt.datetime.now().hour

print(sunrise, sunset, time_now)

