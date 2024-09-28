import os
import smtplib
from datetime import datetime
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")
AMADEUS_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
ISO_DATETIME_FORMAT = "%Y-%m-%d"

FROM_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def compose_alert_message(home_city, round_flight_data):
    home = f"{home_city["name"]}-{home_city["iata_code"]}"
    destination = f"{round_flight_data["target_city"].title()}-{round_flight_data["target_city_airport_iata_code"]}"
    price = f"{float(round_flight_data["total"])} USD"
    from_home_date = datetime.strptime(round_flight_data["trip_start_date"], "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')
    to_home_date = datetime.strptime(round_flight_data["trip_end_date"], "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d')
    transfers = round_flight_data["transfers"]

    base_message = (f"Low price alert!\n\n"
                    f"Only {price} from {home} to {destination}, "
                    f"on {from_home_date} "
                    f"until {to_home_date}")

    if transfers > 0:
        return base_message + f"\n\nPlease keep in mind it is not a direct flight.\nAmount of transfers: {transfers}"
    else:
        return base_message


def send_email(customer, home_city, round_flight_data):
    with smtplib.SMTP("smtp.gmail.com") as client:
        client.starttls()
        client.login(user=FROM_EMAIL, password=PASSWORD)
        client.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=customer["email"],
            msg=f"Subject:Best Flight Deal Notification\n\n{compose_alert_message(home_city, round_flight_data)}"
        )


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.send_email = send_email

    def send_message(self, home_city, round_flight_data):
        self.client.messages.create(
            body=compose_alert_message(home_city, round_flight_data),
            from_=TWILIO_NUMBER,
            to=PERSONAL_NUMBER,
        )
