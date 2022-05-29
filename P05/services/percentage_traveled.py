# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:41:04 2022

@author: victo

"""
#For each connection station, determine the next possible connection
#including travel time, and calculate the percentage of the trip covered when reaching the connection station, 
#again using line of sight. Moreover, give a travel recommendation to the user, including the next possible connection and where to
#search for follow-up connections.

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
        self.starting = loc['from']['coordinate']
        self.start_x = starting['x']
        self.start_y = starting['y']

        self.ending = loc['to']['coordinate']
        self.end_x = ending['x']
        self.end_y = ending['y']  

        self.destination_x = 0
        self.destination_y = 0



    def calculate_distance(self):
    
        if end_x == self.destination_x and end_y == self.destination_y:
            print('We are able to fullfill 100% of the trip thorugh our Connections')
        else:
        #calculate total distance
            self.coords_1 = (self.start_x,self.start_y)
            self.coords_2 = (self.destination_x,self.destination_y)
            self.total_distance = (geopy.distance.geodesic(self.coords_1,self.coords_2).km)
        #calculate reachable distance
            self.coords_1 = (start_x,start_y)
            self.coords_2 = (end_x,end_y)
            self.reachable_distance = (geopy.distance.geodesic(self.coords_1, self.coords_2).km)
        #calculate how much of the way has been reached through our app
            self.percent = (self.total_distance / 100) / self.reachable_distance
            return self.percent

def travel_time(self):
     self.duration = loc['connections'][0]['duration']
     return self.duration

if __name__ == '__main__':
    Calculator.calculate_distance()
    Calculator.travel_time()
