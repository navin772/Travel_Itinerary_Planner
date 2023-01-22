import requests
import json
from flight_data import get_flight_data 
from hotel_data import get_hotel_data
from events_data import get_events_data
from transportation_data import get_transportation_data

# Gather information from different APIs 
def gather_information(source, destination, start_date, end_date, budget, interests):

    flight_data = get_flight_data(source, destination, start_date, budget)
    hotel_data = get_hotel_data(destination, start_date, end_date, budget)
    activity_data = get_events_data(destination, interests, budget)
    transportation_data = get_transportation_data(destination)

    return flight_data, hotel_data, activity_data, transportation_data

# Use an algorithm to determine the best itinerary option
def determine_itinerary(budget, flight_data, hotel_data, activity_data, transportation_data):

    best_itinerary = None
    lowest_cost = float('inf')
    for flight in flight_data:
        for hotel in hotel_data:
            for activity in activity_data:
                for transportation in transportation_data:
                    cost = flight['price'] + hotel['price'] + activity['price'] + transportation['price']
                    if cost < lowest_cost:
                        best_itinerary = {
                            'flight': flight,
                            'hotel': hotel,
                            'activity': activity,
                            'transportation': transportation
                        }
                        lowest_cost = cost
    return best_itinerary

# Create itinerary
def create_itinerary(best_itinerary):

    itinerary = {
        'flight': best_itinerary['flight']['itinerary'],
        'hotel': best_itinerary['hotel']['itinerary'],
        'activity': best_itinerary['activity']['itinerary'],
        'transportation': best_itinerary['transportation']['itinerary'],
        'cost': best_itinerary['flight']['price'] + best_itinerary['hotel']['price'] + best_itinerary['activity']['price'] + best_itinerary['transportation']['price']
    }
    return itinerary

# Suggest additional options
def suggest_additional_option(source, destination, start_date, end_date, budget, itinerary, interests):

    additional_options = []
    increased_budget = budget + (budget * 0.05) # 5% increase in budget
    options = gather_information(source, destination, start_date, end_date, increased_budget, interests)
    best_itinerary = determine_itinerary(increased_budget, *options)
    additional_options.append(create_itinerary(best_itinerary))

    return additional_options

# Present the itinerary
def present_itinerary(itinerary, additional_options):
    print("Best Itinerary:")
    print("Flight:", itinerary['flight'])
    print("Hotel:", itinerary['hotel'])
    print("Activity:", itinerary['activity'])
    print("Transportation:", itinerary['transportation'])
    print("Total cost:", itinerary['cost'])
    print("Additional options:")
    for i, option in enumerate(additional_options):
        print(f"Option {i+1}:")
        print("Flight:", option['flight'])
        print("Hotel:", option['hotel'])
        print("Activity:", option['activity'])
        print("Transportation:", option['transportation'])
        print("Total cost:", option['cost'])
