from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flightSearch = FlightSearch()

cities = data_manager.get_destination_cities()
