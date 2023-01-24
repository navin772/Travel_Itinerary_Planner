# get hotel data
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()


def get_hotel_data(destination, start_date, end_date, budget):

    # Get hotel data from an API
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q":destination,"locale":"en_US","langid":"1033","siteid":"300000001"}

    headers = {
        "X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    obj = json.loads(response.text)
    json_formatted_data = json.dumps(obj, indent=2)
    # print(json_formatted_data)
    #process response here and store hotel names in organized_hotel_data
    organized_hotel_data = []
    
    return organized_hotel_data

get_hotel_data("new delhi", "2020-01-01", "2020-01-02", 100)