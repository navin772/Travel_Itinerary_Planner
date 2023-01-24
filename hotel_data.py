# get hotel data
import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

def get_hotel_data(code, start_date, end_date, budget):
    url = "https://travel-advisor.p.rapidapi.com/hotels/list"

    querystring = {"location_id":code,"adults":"1","rooms":"1","nights":"2","offset":"0","currency":"USD","order":"asc","limit":"25","lang":"en_US"}

    headers = {
        "X-RapidAPI-Key": "7e2044af5fmsh645c3016f861157p104f11jsnca6fe90724fe",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['data']
