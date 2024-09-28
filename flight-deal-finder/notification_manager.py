import os
from datetime import datetime
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")
AMADEUS_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
ISO_DATETIME_FORMAT = "%Y-%m-%d"


# TODO: Define incoming time format
def compose_alert_message(home_city, round_flight_data):
    home = f"{home_city["name"]}-{home_city["iata_code"]}"
    destination = f"{round_flight_data["target_city"].title()}-{round_flight_data["target_city_airport_iata_code"]}"
    price = f"${float(round_flight_data["total"])}"
    from_home_date = datetime.strptime(round_flight_data["trip_start_date"], "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')
    to_home_date = datetime.strptime(round_flight_data["trip_end_date"], "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')

    return (f"Low price alert! Only {price} from {home} to {destination},"
            f" on {from_home_date}"
            f" until {to_home_date}")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_message(self, home_city, round_flight_data):
        self.client.messages.create(
            body=compose_alert_message(home_city, round_flight_data),
            from_=TWILIO_NUMBER,
            to=PERSONAL_NUMBER,
        )
