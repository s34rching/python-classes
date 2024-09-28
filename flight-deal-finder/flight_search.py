from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from requests.auth import HTTPBasicAuth
import os
import requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")
BASE_URL = "https://test.api.amadeus.com"
GET_TOKEN_ENDPOINT = f"{BASE_URL}/v1/security/oauth2/token"
FLIGHT_OFFERS_ENDPOINT = f"{BASE_URL}/v2/shopping/flight-offers"
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
        self.home_city = "Denver"
        self.home_city_iata_code = "DEN"
        self.currency = "USD"
        self.client = requests.Session()
        self.refresh_token()

    def get_home_city(self):
        return {
            "name": self.home_city,
            "iata_code": self.home_city_iata_code
        }

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
            "Authorization": os.environ["AMADEUS_TOKEN"]
        }

        params = {
            "countryCode": country_code,
            "keyword": name.upper(),
            "max": 10,
            "include": ["AIRPORTS"]
        }

        response = requests.get(CITIES_ENDPOINT, params=params, headers=headers)
        return response.json()

    def get_flights(self, city_iata_code):
        self.refresh_token()

        months = 6
        tomorrow = datetime.now() + relativedelta(days=+1)
        in_six_months = tomorrow + relativedelta(months=+months)
        from_date = tomorrow.strftime(ISO_DATETIME_FORMAT)
        to_date = in_six_months.strftime(ISO_DATETIME_FORMAT)

        headers = {
            "Authorization": os.environ["AMADEUS_TOKEN"]
        }

        params = {
            "originLocationCode": self.home_city_iata_code,
            "destinationLocationCode": city_iata_code,
            "departureDate": from_date,
            "returnDate": to_date,
            "currencyCode": self.currency,
            "adults": 1,
            "nonStop": 'true',
        }

        response = requests.get(FLIGHT_OFFERS_ENDPOINT, params=params, headers=headers)
        return response.json()
