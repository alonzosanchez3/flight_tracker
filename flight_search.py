import requests
from dotenv import load_dotenv
import os

load_dotenv()

ENDPOINT = os.getenv('TEQUILA_ENDPOINT')
LOCATIONS_API = os.getenv('LOCATIONS_API')


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        config = {
            'term': city_name,
            'location_types': 'city'
        }
        headers = {
            'apikey': LOCATIONS_API
        }
        response = requests.get(url=f"{ENDPOINT}/locations/query", params=config, headers=headers)
        data = response.json()
        code = data['locations'][0]['code']
        return code