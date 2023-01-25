# get hotel data
import os
from dotenv import load_dotenv
import json
import requests
import datetime

load_dotenv()

def find_nights(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    nights = (end_date - start_date).days
    return nights

def get_hotel_data(code, start_date, end_date):

    url = "https://travel-advisor.p.rapidapi.com/hotels/list"

    querystring = {"location_id":code,"adults":"1","rooms":"1","nights": find_nights(start_date, end_date),"checkin":start_date, "offset":"0","currency":"USD","order":"asc","limit":"25","lang":"en_US"}

    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    hotels = {}
    for i in range(len(data['data'])):
        if all(k in data['data'][i].keys() for k in ('price', 'name')):
            price = data['data'][i]['price'].split()[-1]   #price in USD
            price = float(price[1:])
            hotels[data['data'][i]['name']] = price    
        else:
            pass
    hotels = {k: v for k, v in sorted(hotels.items(), key=lambda item: item[1])}
    new_hotels = {}
    j = 1
    for keys in hotels.keys():
        new_hotels[j] = {'name': keys, 'price': hotels[keys]}
        j += 1

    return new_hotels

# hotel = get_hotel_data(304551, "2023-02-01", "2023-02-15")
# print(hotel)
