import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = os.getenv('SHEETY_ENDPOINT')
        