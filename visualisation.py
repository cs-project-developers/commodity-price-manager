from geopy.geocoders import Nominatim
import geopy.distance as dist
import tkintermapview

def get_long_lat(location):
    geolocator = Nominatim(user_agent="cpm")
    convert_location = geolocator.geocode(location)
    return convert_location.longitude, convert_location.latitude

def get_distance(location_1,location_2):
    return dist.distance(location_1,location_2).km

def shortest_dist(distances):
    buffer_list = []
    for i in distances:
        buffer_list.append(i[2])
    min_dist = min(buffer_list)
    index = buffer_list.find(min_dist)
    return distances[index]
