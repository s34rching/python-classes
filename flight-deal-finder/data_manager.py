from flight_search import FlightSearch
import os
import requests

SHEETY_FLIGHTS_ENDPOINT = os.environ.get("SHEETY_FLIGHTS_ENDPOINT")


class DataManager:
    def __init__(self):
        self.client = requests.Session()
        self.destination_cities = self.load_data()
        self.set_iata_codes()

    def load_data(self):
        headers = {
            "Authorization": os.environ.get("SHEETY_FLIGHTS_AUTH_TOKEN")
        }

        response = self.client.get(SHEETY_FLIGHTS_ENDPOINT, headers=headers)
        data = response.json()
        return data["cities"]

    def update_row(self, row_id, data):
        headers = {
            "Authorization": os.environ.get("SHEETY_FLIGHTS_AUTH_TOKEN")
        }

        self.client.put(f"{SHEETY_FLIGHTS_ENDPOINT}/{row_id}", json=data, headers=headers)

    def set_iata_codes(self):
        flight_search = FlightSearch()

        for city in self.destination_cities:
            if len(city["iataCode"]) < 3:
                iata_data = flight_search.get_city(city["city"], city["countryCode"])
                iata_city_code = iata_data["data"][0]["iataCode"]

                city["iataCode"] = iata_city_code

                payload = {
                    "city": {
                        "iataCode": iata_city_code,
                    }
                }

                self.update_row(city["id"], payload)

    def get_destination_cities(self):
        return self.destination_cities
