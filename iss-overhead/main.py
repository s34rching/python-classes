import requests
import time
from datetime import datetime
import pytz
import smtplib
import os

ISO_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
LAT = 52.2084429
LNG = 20.9264266
FROM_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def is_dark_sky(sunrise, sunset):
    now = datetime.now(tz=pytz.timezone("Europe/Warsaw"))
    sunrise_time = datetime.strptime(sunrise, ISO_FORMAT)
    sunset_time = datetime.strptime(sunset, ISO_FORMAT)

    return now < sunrise_time or now > sunset_time


def is_iss_visible(iss_position):
    iss_lat = float(iss_position["latitude"])
    iss_lng = float(iss_position["longitude"])

    return 5 >= LAT - iss_lat >= - 5 and 5 >= LNG - iss_lng >= -5


params = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()

ss_response = requests.get("https://api.sunrise-sunset.org/json", params=params)
ss_data = ss_response.json()
sunrise_t = ss_data["results"]["sunrise"]
sunset_t = ss_data["results"]["sunset"]

is_tracking = True

while is_tracking:
    if is_dark_sky(sunrise_t, sunset_t):
        iss_response = requests.get("http://api.open-notify.org/iss-now.json")
        iss_data = iss_response.json()

        if is_iss_visible(iss_data["iss_position"]):
            with smtplib.SMTP("smtp.gmail.com") as client:
                client.starttls()
                client.login(user=FROM_EMAIL, password=PASSWORD)
                client.sendmail(
                    from_addr=FROM_EMAIL,
                    to_addrs=FROM_EMAIL,
                    msg=f"Subject:ISS is visible!\n\nHurry up to see it in the sky!"
                )

        is_tracking = False

    time.sleep(10)
