import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
HEADERS = {
    "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_request(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def put_request(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}', headers=HEADERS, json=new_data)

