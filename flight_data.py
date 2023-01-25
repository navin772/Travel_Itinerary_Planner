# get flight data
import os
from dotenv import load_dotenv
import requests
from get_location import get_locationId

load_dotenv()

def text_to_code(text):
    # convert text to airport code
    url = "https://aerodatabox.p.rapidapi.com/airports/search/term"

    querystring = {"q":text,"limit":"10"}

    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['items'][0]['iata']


def get_flight_data(source, destination, date):
    # date format: YYYY-MM-DD
    # Get flight data from an API
    source = text_to_code(source)
    destination = text_to_code(destination)
    url = "https://skyscanner50.p.rapidapi.com/api/v1/searchFlights"

    querystring = {"origin":source,"destination":destination,"date":date,"adults":"1","currency":"USD","countryCode":"US","market":"en-US"}

    headers = {
        "X-RapidAPI-Key": '16ad3426e0msh021039bc5b9f44ap1d1f08jsna850e721ad07',
        "X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    flight_data = response.json()
    flight_data_1 = {}
    
    for i in range (len(flight_data['data'])):
        price = flight_data['data'][i]['price']['amount']
        flight_data_1[flight_data['data'][i]['legs'][0]['carriers'][0]['name']] = price

    flight_data_1 = {k: v for k, v in sorted(flight_data_1.items(), key=lambda item: item[1])}
    new_flight_data = {}
    j = 1
    for keys in flight_data_1.keys():
        new_flight_data[j] = {'name': keys, 'price': flight_data_1[keys]}
        j += 1

    return new_flight_data
 
# print(get_flight_data('new delhi', 'mumbai', '2023-02-01'))