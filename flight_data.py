# get flight data
import os
from dotenv import load_dotenv
import requests

load_dotenv()

def text_to_code(text):
    # convert text to airport code
    url = "https://aerodatabox.p.rapidapi.com/airports/search/term"

    querystring = {"q":text,"limit":"10"}

    headers = {
        "X-RapidAPI-Key": "e42d97ca3bmsh173d6fe9aba63d8p1d4c07jsna586a8662638",
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['items'][0]['iata']


def get_flight_data(source, destination, date, budget):
    # date format: YYYY-MM-DD
    # Get flight data from an API
    source = text_to_code(source)
    destination = text_to_code(destination)
    url = "https://skyscanner50.p.rapidapi.com/api/v1/searchFlights"

    querystring = {"origin":source,"destination":destination,"date":date,"adults":"1","currency":"USD","countryCode":"US","market":"en-US"}

    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    flight_data = response.text

    return flight_data
