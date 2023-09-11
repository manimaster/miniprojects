import requests

# Replace 'YOUR_BING_MAPS_API_KEY' with your actual Bing Maps API key
api_key = 'YOUR_BING_MAPS_API_KEY'

def get_directions(api_key, origin, destination):
    base_url = 'https://dev.virtualearth.net/REST/v1/Routes/Driving'

    params = {
        'key': api_key,
        'wayPoint.1': origin,
        'wayPoint.2': destination,
        'optimize': 'time',  # You can change this to 'distance' if you want to optimize for distance
        'format': 'json',
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print("Error fetching directions.")
        return

    data = response.json()

    if 'resourceSets' in data and len(data['resourceSets']) > 0 and 'resources' in data['resourceSets'][0]:
        route = data['resourceSets'][0]['resources'][0]

        distance = route['travelDistance']
        duration = route['travelDuration']

        print(f"Directions from {origin} to {destination}:")
        print(f"Distance: {distance} km")
        print(f"Estimated Duration: {duration} seconds")
    else:
        print("No directions found between the specified locations.")

if __name__ == "__main__":
    origin = input("Enter the origin (e.g., 'New York, NY'): ")
    destination = input("Enter the destination (e.g., 'Los Angeles, CA'): ")

    get_directions(api_key, origin, destination)
