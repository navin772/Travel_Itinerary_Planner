# get events data
import requests
import json
import os
import time
from dotenv import load_dotenv
from get_location import get_locationId

load_dotenv()

def get_events_data(code):

    url = "https://travel-advisor.p.rapidapi.com/attractions/list"

    querystring = {"location_id":code ,"currency":"USD","lang":"en_US","lunit":"km","sort":"recommended"}

    headers = {
            "X-RapidAPI-Key": "e42d97ca3bmsh173d6fe9aba63d8p1d4c07jsna586a8662638",
            "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()

    events_data = {}
    for i in range(len(res['data'])):
        if all(k in res['data'][i].keys() for k in ('offer_group', 'name')):
            
            price = res['data'][i]['offer_group']['lowest_price']  
            price = float(price[1:])
            
            events_data[res['data'][i]['name']] = price
                
        else:
            pass

    events_data = {k: v for k, v in sorted(events_data.items(), key=lambda item: item[1])}
    new_events_data = {}
    j = 1
    for keys in events_data.keys():
        new_events_data[j] = {'name': keys, 'price': events_data[keys]}
        j += 1
    return new_events_data

# print(get_events_data(304551))
