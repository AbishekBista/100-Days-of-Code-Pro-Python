import requests
from datetime import datetime
import smtplib
from secret import MY_LAT, MY_LONG, MY_EMAIL, PASSWORD, RECIPIENT
import time

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.

def check_for_margin(my_lat, my_long):
    if iss_latitude >= my_lat - 5 and iss_latitude <= my_lat + 5:
        if iss_longitude >= my_lat + 5 and iss_longitude <= my_long + 5:
            return True
    return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kathmandu"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

print(sunrise)
print(sunset)
print(time_now)

while True:
    time.sleep(60)
    if time_now >= sunset or time_now <= sunrise:
        if check_for_margin(MY_LAT, MY_LONG):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT, msg="Subject:ISS Above You\n\nLook above, the ISS is flying above you!")
        



