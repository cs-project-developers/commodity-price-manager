from pprint import pprint
from geopy.geocoders import Nominatim
import geopy.distance as dist
import geocoder
#use latitude and longitude in the same order
def get_long_lat(location):
    geolocator = Nominatim(user_agent="cpm")
    if location.split(" ")[-1] == "Mandi":
        location = location.split(" ")[0]
    elif location.split("("):
        location = location.split("(")[0]
    try:
        convert_location = geolocator.geocode(location)
        return convert_location.latitude , convert_location.longitude    
    except:
        pass

def get_distance(location_1,location_2):
    return float(dist.distance(location_1,location_2).km)

def shortest_dist(distances):
    buffer_list = []
    for i in distances:
        buffer_list.append(i[1])
    min_dist = min(buffer_list)
    index = buffer_list.index(min_dist)
    return distances[index]

user_current_location = geocoder.ip('me').latlng

def generate_shortest_dist(locations):
    result_list = list()
    for i in locations:
        long_lat = get_long_lat(i)
        get_dist = get_distance(user_current_location,long_lat)
        result = [i,get_dist]
    
        result_list.append(result)
    shortest_distance = shortest_dist(result_list)
    return shortest_distance
