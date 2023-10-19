#generate gps coordinates using python
from geopy.geocoders import Nominatim
import requests
import pandas as pd

#get the coordinates of the address

# def get_coordinates(address):
#     geolocator = Nominatim(user_agent="myapplication")
#     location = geolocator.geocode(address)
#     return location.latitude, location.longitude

# # print the coordinates of the address
# def print_coordinates(address):
#     lat, lon = get_coordinates(address)
#     print("Latitude: ", lat)
#     print("Longitude: ", lon)

# get_coordinates("1600 Amphitheatre Parkway, Mountain View, CA")
# print_coordinates("1600 Amphitheatre Parkway, Mountain View, CA")

city = "Moscow,RU"
city_id = 0
app_id = "7d97302422b2c1b2a0bb6cb8327a064d"

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': 
                 app_id})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)

except Exception as e:
    print("Exception (find):", e)
    pass

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass