from geopy.distance import vincenty
import json
import os 


def load_data(filepath):
    try:
        with open(filepath, "r", encoding='cp1251') as data_file:
            bars_data = json.load(data_file)
            return bars_data
    except FileNotFoundError:
        print('File not found!')
        return None


def get_bar_locations(bars_data):
    bar_locations = []
    for each_bar in bars_data:
        bar_location = (each_bar['Longitude_WGS84'], each_bar['Latitude_WGS84'])
        bar_locations.append(bar_location)
    return bar_locations


def get_biggest_bar(bars_data):
    biggest_bar = max(bars_data, key=lambda bar_seats: bar_seats['SeatsCount'])
    return biggest_bar['Address']


def get_smallest_bar(bars_data):
    smallest_bar = min(bars_data, key=lambda bar_seats: bar_seats['SeatsCount'])
    return smallest_bar['Address']


def get_user_coordinates():
    try:
        user_longitude = float(input('Your longitude: '))
        user_latitude = float(input('Your latitude: '))
        return user_longitude, user_latitude
    except ValueError:
        print('That is not a number!')
        return None


def get_closest_bar(user_longitude, user_latitude, bar_locations):
    user_location = (user_longitude, user_latitude)
    distance_to_bar = min(bar_locations, key=lambda closest_bar: bar_locations)
    closest_bar = vincenty(distance_to_bar, user_location).meters
    return closest_bar


if __name__ == '__main__':
    filepath = input('Enter the path to .json file: ')
    data_loading = load_data(filepath)
    bar_locations = get_bar_locations(data_loading)
    biggest_bar = get_biggest_bar(data_loading)
    print('The biggest bar: ', biggest_bar)
    smallest_bar = get_smallest_bar(data_loading)
    print('The smallest bar: ', smallest_bar)
    user_coordinates = get_user_coordinates()
    closest_bar = get_closest_bar(user_coordinates[0], user_coordinates[1], bar_locations)
    print('Minimal distance to bar: %s meters' % str(closest_bar))
