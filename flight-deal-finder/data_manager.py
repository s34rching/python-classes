import os
import requests

SHEETY_FLIGHTS_ENDPOINT = os.environ.get("SHEETY_FLIGHTS_ENDPOINT")
SHEETY_FLIGHTS_AUTH_TOKEN = os.environ.get("SHEETY_FLIGHTS_AUTH_TOKEN")


class DataManager:
    def __init__(self):
        self.headers = {
            "Authorization": SHEETY_FLIGHTS_AUTH_TOKEN
        }
        self.client = requests.Session()

    def load_data(self):
        response = self.client.get(SHEETY_FLIGHTS_ENDPOINT, headers=self.headers)
        data = response.json()
        return data["cities"]

    def update_row(self, row_id, data):
        self.client.put(f"{SHEETY_FLIGHTS_ENDPOINT}/{row_id}", json=data, headers=self.headers)
