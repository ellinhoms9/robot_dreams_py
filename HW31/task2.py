import requests


def get_coordinates(city):
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
    data = response.json()
    if "results" in data:
        result = data["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]
        return latitude, longitude
    return None


city = input("Please enter city name: ")
coordinates = get_coordinates(city)

if coordinates:
    latitude, longitude = coordinates
    res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
    list_of_temperatures = res.json()["hourly"]["temperature_2m"]
    print(list_of_temperatures)
else:
    print("Incorrect input")
