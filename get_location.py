import json
import requests

def get_locationId(destination):
    url = "https://travel-advisor.p.rapidapi.com/locations/search"

    querystring = {"query":destination,"limit":"1","offset":"0","units":"km","location_id":"1","currency":"USD","sort":"relevance","lang":"en_US"}

    headers = {
	    "X-RapidAPI-Key": "7e2044af5fmsh645c3016f861157p104f11jsnca6fe90724fe",
	    "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # response.text.loads(response.text)
    return response.json()['data'][0]['result_object']['location_id']

