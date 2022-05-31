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


class DistanceCalculator:

    def calculate_closest_location(self, reachable_stations, destination_station, start_station):
        closest_distance = 200000000
        closest_station = None
        link = self.alternate_link(destination_station)
        destination_coord = (destination_station.long, destination_station.lat)
        total_distance = (geopy.distance.geodesic((start_station.long, start_station.lat), destination_coord).km)
        for station in reachable_stations:

            # calculate closest reachable station
            temp_coord = (station.long, station.lat)
            temp_distance = (geopy.distance.geodesic(temp_coord, destination_coord).km)
            if station and temp_distance < closest_distance:
                closest_distance = temp_distance
                closest_station = station

        return self.calculate_percent_and_time(total_distance,closest_station, start_station,link)

    def calculate_percent_and_time(self,total_distance ,closest_station, start_station,link):
        coords_1 = (start_station.long,start_station.lat)
        coords_2 = (closest_station.long,closest_station.lat)
        reachable_distance = (geopy.distance.geodesic(coords_1,coords_2).km)
        # calculate how much of the way has been reached through our app
        percent = round((reachable_distance/total_distance) * 100, 2)
        duration = self.travel_time(start_station.city,closest_station.city)
        return f'Closest Location to your final Destination: {closest_station.city}\n' \
               f'{percent}% of the way travelled\n' \
               f'Duration: {duration}\n' \
               f'More Info at: {link}'




    def travel_time(self, start_station, closest_station):
        link = f'http://transport.opendata.ch/v1/connections?from={start_station}&to={closest_station}'
        r = requests.get(link)
        loc = r.json()
        return loc['connections'][0]['duration']

    def alternate_link(self,destination_station):
        searchlinks = {'Niederlände': 'https://www.connexxion.nl/de/fahrkarten',
                       'Spanien': 'https://www.renfe.com/es/es',
                       'Deutschland': 'https://www.bahn.de/',
                       'Österreich': 'https://www.oebb.at/',
                       'Italien': 'https://www.trenitalia.com/de.html',
                       'Belgien': 'https://www.belgiantrain.be/de'}
        try:
            link = searchlinks[destination_station.country]
            return link
        except KeyError:
            link = ''
            return link



