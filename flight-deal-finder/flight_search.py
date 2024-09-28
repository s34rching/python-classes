from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from requests.auth import HTTPBasicAuth
import os
import requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")
BASE_URL = "https://test.api.amadeus.com"
GET_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CHEAP_FLIGHTS_ENDPOINT = f"{BASE_URL}/v1/shopping/flight-dates"
CITIES_ENDPOINT = f"{BASE_URL}/v1/reference-data/locations/cities"
TOKEN_EXPIRES_IN_SECONDS = 1799
ENVIRONMENT_RESERVED_SECONDS = 5
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
ISO_DATETIME_FORMAT = "%Y-%m-%d"


def is_token_valid() -> bool:
    def is_expired(last_refreshed) -> bool:
        expired = datetime.strptime(last_refreshed, DATETIME_FORMAT) + timedelta(seconds=TOKEN_EXPIRES_IN_SECONDS)

        return datetime.now() > expired

    token = os.environ.get("AMADEUS_TOKEN")
    token_last_refreshed = os.environ.get("AMADEUS_TOKEN_LAST_REFRESHED")

    if token is None or token_last_refreshed is None:
        return False

    if is_expired(token_last_refreshed):
        return False

    return True


class FlightSearch:
    def __init__(self):
        self.client = requests.Session()
        self.refresh_token()

    def refresh_token(self):
        if not is_token_valid():
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }

            data = {
                "grant_type": "client_credentials",
            }

            response = self.client.post(
                GET_TOKEN_ENDPOINT,
                data=data,
                auth=HTTPBasicAuth(AMADEUS_API_KEY, AMADEUS_API_SECRET),
                headers=headers)

            auth_data = response.json()

            last_refreshed = (datetime.now() - timedelta(ENVIRONMENT_RESERVED_SECONDS)).strftime(DATETIME_FORMAT)

            os.environ["AMADEUS_TOKEN"] = f"Bearer {auth_data['access_token']}"
            os.environ["AMADEUS_TOKEN_LAST_REFRESHED"] = last_refreshed

    def get_city(self, name, country_code):
        self.refresh_token()

        headers = {
            {"Authorization": os.environ["AMADEUS_TOKEN"]}
        }

        params = {
            "countryCode": country_code,
            "keyword": name.upper(),
            "max": 10,
            "include": ["AIRPORTS"]
        }

        response = requests.get(CITIES_ENDPOINT, params=params, headers=headers)
        return response.json()

    def get_flights(self):
        months = 2
        now = datetime.now()
        in_six_months = now + relativedelta(months=+months)
        from_time = now.strftime(ISO_DATETIME_FORMAT)
        to_time = in_six_months.strftime(ISO_DATETIME_FORMAT)

        self.refresh_token()

        headers = {
            {"Authorization": os.environ["AMADEUS_TOKEN"]}
        }

        params = {
            "origin": "BKK",
            "destination": "CNX",
            "departureDate": f"{from_time},{to_time}",
            "currencyCode": "USD"
        }

        response = requests.get(CHEAP_FLIGHTS_ENDPOINT, params=params, headers=headers)
        return response.json()
