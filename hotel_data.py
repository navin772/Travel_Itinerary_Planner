# get hotel data
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

def get_hotel_data(code):
    url = "https://travel-advisor.p.rapidapi.com/hotels/list"

    querystring = {"location_id":code,"adults":"1","rooms":"1","nights":"2","offset":"0","currency":"USD","order":"asc","limit":"25","lang":"en_US"}

    headers = {
        "X-RapidAPI-Key": "7e2044af5fmsh645c3016f861157p104f11jsnca6fe90724fe",
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

    return hotels
