from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search_manager = FlightSearch()
notifications_manager = NotificationManager()

home_city = flight_search_manager.get_home_city()
cities = data_manager.get_destination_cities()
customers = data_manager.get_destination_cities()

for city in cities:
    flights_data = flight_search_manager.get_flights(city["iataCode"])

    flight_data_manager = FlightData(city)
    result = flight_data_manager.find_lowest_price(flights_data)

    if result["success"]:
        for customer in customers:
            notifications_manager.send_email(customer, home_city, result["data"])
