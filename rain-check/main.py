import os
import requests
from twilio.rest import Client

LAT = 43.4612345
LNG = 13.7435346

OWM_KEY = os.environ.get("OWM_KEY")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": LAT,
    "lon": LNG,
    "appid": OWM_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=params)
data = response.json()

next_hours_conditions = [time_point["weather"][0]["id"] for time_point in data["list"]]

is_umbrella_needed = False

for condition in next_hours_conditions:
    if condition < 700:
        is_umbrella_needed = True

if is_umbrella_needed:
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body="Take your umbrella. It is about to rain today.",
        from_=TWILIO_NUMBER,
        to=PERSONAL_NUMBER
    )
