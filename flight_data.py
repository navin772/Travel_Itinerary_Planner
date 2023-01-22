# get flight data
import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_flight_data(source, destination, date, budget):
    # date format: YYYY-MM-DD
    # Get flight data from an API
    url = "https://skyscanner50.p.rapidapi.com/api/v1/searchFlights"

    querystring = {"origin":source,"destination":destination,"date":date,"adults":"1","currency":"USD","countryCode":"US","market":"en-US"}

    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    flight_data = []

    return flight_data