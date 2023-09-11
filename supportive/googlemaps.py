# 2019 Version
# Changes over time

import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

def get_directions(api_key, origin, destination):
    gmaps = googlemaps.Client(key=api_key)

    # Geocoding the origin and destination to ensure proper place names
    origin_geocode = gmaps.geocode(origin)
    destination_geocode = gmaps.geocode(destination)

    if not origin_geocode or not destination_geocode:
        print("Invalid origin or destination. Please check the place names.")
        return

    # Extracting proper place names
    origin = origin_geocode[0]['formatted_address']
    destination = destination_geocode[0]['formatted_address']

    # Requesting directions
    directions = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())

    if not directions:
        print("No directions found between the specified locations.")
        return

    route = directions[0]['legs'][0]

    distance = route['distance']['text']
    duration = route['duration']['text']

    print(f"Directions from {origin} to {destination}:")
    print(f"Distance: {distance}")
    print(f"Estimated Duration: {duration}")

if __name__ == "__main__":
    origin = input("Enter the origin (e.g., 'New York, NY'): ")
    destination = input("Enter the destination (e.g., 'Los Angeles, CA'): ")

    get_directions(api_key, origin, destination)
