from datetime import datetime, timedelta
import os
import requests

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")
GET_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
TOKEN_EXPIRES_IN_SECONDS = 1799
ENVIRONMENT_RESERVED_SECONDS = 5
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


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

    def refresh_token(self):
        if not is_token_valid():
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }

            data = {
                "grant_type": "client_credentials",
                "client_id": AMADEUS_API_KEY,
                "client_secret": AMADEUS_API_SECRET,
            }

            response = self.client.post(GET_TOKEN_ENDPOINT, json=data, headers=headers)
            auth_data = response.json()

            last_refreshed = (datetime.now() - timedelta(ENVIRONMENT_RESERVED_SECONDS)).strftime(DATETIME_FORMAT)

            os.environ["AMADEUS_TOKEN"] = f"{auth_data['token_type']} {auth_data['access_token']}"
            os.environ["AMADEUS_TOKEN_LAST_REFRESHED"] = last_refreshed
