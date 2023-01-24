# get events data
import requests
import json
from get_location import get_locationId

def get_events_data(code, destination, interests, budget):

    # Get events data from an API
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
            
            events_data[res['data'][i]['name']] = res['data'][i]['offer_group']['lowest_price']
            
        else:
            pass
    
    return events_data

print(get_events_data(get_locationId("new delhi"), "delhi", ["Museums", "Landmarks"], 1000))