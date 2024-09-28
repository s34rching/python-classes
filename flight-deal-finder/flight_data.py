class FlightData:
    def __init__(self, destination_city):
        self.target_city = destination_city

    def find_lowest_price(self, flights_data):
        if 'data' not in flights_data:
            return {
                "success": "False",
                "message": "Something went wrong",
                "data": None
            }

        if len(flights_data["data"]) == 0 or flights_data["data"] is None:
            return {
                "success": "False",
                "message": "No flights data found",
                "data": None
            }

        flights = flights_data["data"]

        lowest_price_flight = next(flight for flight in flights if float(flight["price"]["grandTotal"]) < self.target_city["lowestPrice"])
        round_trip_details = lowest_price_flight["itineraries"]
        from_home_flight_departure = round_trip_details[0]["segments"][0]
        to_home_flight_departure = round_trip_details[1]["segments"][0]
        transfers = len(round_trip_details[0]["segments"]) - 1

        return {
            "success": True,
            "message": None,
            "data": {
                "target_city": self.target_city["city"],
                "target_city_airport_iata_code": self.target_city["iataCode"],
                "transfers": transfers,
                "trip_start_date": from_home_flight_departure["departure"]["at"],
                "trip_end_date": to_home_flight_departure["departure"]["at"],
                "total": lowest_price_flight["price"]["grandTotal"]
            }
        }
