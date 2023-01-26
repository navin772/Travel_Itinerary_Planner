from fastapi import FastAPI
import uvicorn

from flight_data import get_flight_data 
from hotel_data import get_hotel_data
from events_data import get_events_data
from get_location import get_locationId

best_itinerary = {}
app = FastAPI()

@app.get('/get_itinerary/', status_code=200)
def preferences(source: str, destination: str, start_date: str, end_date: str, budget: float):

    # Gather information from different APIs 
    options = gather_information(source, destination, start_date, end_date)

    # Use an algorithm to determine the itinerary option
    best_itinerary = determine_itinerary(budget, True, *options)
    additional_itinerary = determine_itinerary(budget + (budget * 0.05), False, *options)

    # Create itinerary
    global_itinerary = {
        'best_itinerary': best_itinerary,
        'additional_itinerary': additional_itinerary
    }

    return global_itinerary

# Gather information from different APIs 
def gather_information(source, destination, start_date, end_date):

    code = get_locationId(destination)

    # flight_data = get_flight_data(source, destination, start_date)
    hotel_data = get_hotel_data(code, start_date, end_date)
    activity_data = get_events_data(code)

    return hotel_data, activity_data

# Use an algorithm to determine the best itinerary option
def determine_itinerary(budget, flag, hotel_data, activity_data):
    best_itinerary = []
    for i in range(1, 25):
        if i > len(hotel_data) or i > len(activity_data):
            break
        cost = hotel_data[i]['price'] + activity_data[i]['price']
        if cost > budget:
            break
        else:
            if flag and len(best_itinerary) > 0:
                break
            if flag != True and len(best_itinerary) > 1:
                break
            best_itinerary.append({
                'hotel': hotel_data[i],
                'activity': activity_data[i],
            })
    return best_itinerary