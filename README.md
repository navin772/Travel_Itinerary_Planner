# Travel_Itinerary_Planner

Get detailed travel itinerary based on your budget and interests!

## API usage

Endpoint: travel-itinerary-planner.vercel.app/get_itinerary/
### For use in terminal using CURL
1. Install CURL
2. Run the following command
```bash
curl -X 'GET' 'https://travel-itinerary-planner-navin772.vercel.app/get_itinerary/?source={your_city}&destination={destination_city}&start_date={departure_date}&end_date={returning_date}&budget={budget_in_USD}' -H 'accept: application/json'
```

### For use in browser
1. Open the following link in your browser
```
https://travel-itinerary-planner-navin772.vercel.app/get_itinerary/?source={your_city}&destination={destination_city}&start_date={departure_date}&end_date={returning_date}&budget={budget_in_USD}
```
*`date format: YYYY-MM-DD`*