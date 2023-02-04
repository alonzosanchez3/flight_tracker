from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_request()

if sheet_data[0]['iataCode'] == '':
  from flight_search import FlightSearch
  flight_search = FlightSearch()
  for row in sheet_data:
    row['iataCode'] = flight_search.get_destination_code(row['city'])
  data_manager.destination_data = sheet_data
  data_manager.put_request()




