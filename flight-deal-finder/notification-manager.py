import os
from datetime import datetime
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")


# TODO: Define incoming time format
def compose_alert_message(home, destination, price, time_from, time_to):
    return (f"Low price alert! Only €{round(price, 2)} from {home} to {destination},"
            f" on {datetime.strptime(time_from, '%Y-%m-%d').strftime('%Y-%m-%d')}"
            f" until {datetime.strptime(time_to, '%Y-%m-%d').strftime('%Y-%m-%d')}")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_message(self, home, destination, price, time_from, time_to):
        self.client.messages.create(
            body=compose_alert_message(home, destination, price, time_from, time_to),
            from_=TWILIO_NUMBER,
            to=PERSONAL_NUMBER,
        )
