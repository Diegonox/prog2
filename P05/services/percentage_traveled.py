# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:41:04 2022

@author: victo

"""
# For each connection station, determine the next possible connection
# including travel time, and calculate the percentage of the trip covered when reaching the connection station,
# again using line of sight. Moreover, give a travel recommendation to the user, including the next possible connection and where to
# search for follow-up connections.

import requests
import geopy.distance

r = requests.get('http://transport.opendata.ch/v1/connections?from=Lausanne&to=zurich')
loc = r.json()
starting = loc['from']['coordinate']
start_x = starting['x']
start_y = starting['y']

ending = loc['to']['coordinate']
end_x = ending['x']
end_y = ending['y']


class Calculator():

    def __init__(self):
        pass

    def calculate_closest_location(reachable_stations, destination):
        self.closest_distance = 2000

    for stations in reachable_stations:

        # calculate closest reachable station
        self.coords_1 = (self.start_x, self.start_y)
        self.coords_2 = (destination_x, destination_y)
        self.total_distance = (geopy.distance.geodesic(self.coords_1, self.coords_2).km)
        if self.total_distance < self.closest_distance:
            self.closest_distance = self.total_distance
            coords = self.coords_1
            name = reachable_stations['name']

        else:
            pass
        return calculate_closest_location(self, name, coords)

    def calculate_percent_and_time(self, name, coords):
        self.coords_1 = (start_x, start_y)
        self.coords_2 = coords
        self.reachable_distance = (geopy.distance.geodesic(self.coords_1, self.coords_2).km)
        # calculate how much of the way has been reached through our app
        self.percent = (self.total_distance / 100) / self.reachable_distance
        duration = travel_time(start, name)
        return self.percent, name, self.duration


def travel_time(self, start, name):
    link = 'http://transport.opendata.ch/v1/connections?from=', start, '&to=', name)
    r = requests.get(link)
    loc = r.json()
    self.duration = loc['connections'][0]['duration']
    return self.duration


if __name__ == '__main__':
    Calculator.calculate_distance()
    Calculator.travel_time()
