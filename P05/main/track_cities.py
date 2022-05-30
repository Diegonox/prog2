import json
import csv
from models.station import Station
from services.transport_api_service import TransportApiService

__all__ = ['TrackCities']


class TrackCities:
    def __init__(self):
        self.cities = ['Salzburg', 'Graz',
                       'Bregenz', 'Feldkirch', 'Dornbirn', 'Vienne',
                       'Frankfurt am Main', 'Köln', 'Wallhausen',
                       'Ulm', 'Stuttgart Hbf', 'Freiburg im Breisgau', 'Bodman-Ludwigshafen',
                       'Hamburg', 'Konstanz', 'Ravensburg', 'Karlsruhe',
                       'Arnhem', 'Amsterdam', 'Venlo', 'Den Haag',
                       'Paris', 'Lyon', 'Marseille', 'Mühlhausen',
                       'Besançon', 'Grenoble', 'Nice', 'Charleroi',
                       'London', 'Manchester', 'Liverpool', 'Birmingham', 'Leeds',
                       'Prag',
                       'Dublin', 'Belfast', 'Glasgow',
                       'Cadaqués', 'Málaga', 'Murcia', 'Valencia',
                       'Madrid', 'Saragosa', 'Barcelona', 'Bilbao', 'Valladolid',
                       'Milano', 'Bologna', 'Aosta', 'Domodossola', 'como', 'Varese']

    def create_track_file(self, city_from):
        '''
        creates a json file called 'track_dict' with the connections from the 
        city_from to the cities in the list cities and defines the access as 
        reachable or unreachable
        '''
        transport_api_service = TransportApiService()
        connections = []
        for city in self.cities:
            api_response = transport_api_service.get_connections(city_from, city)
            station = Station()
            station.set_station_by_city(city)
            station.set_station_by_api_response(api_response)
            connections.append(station)

        with open(f'../data/track_{city_from}.csv', 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['city', 'country' 'reachable', 'station_to', 'lat', 'long'])
            for connection in connections:
                writer.writerow(
                    [connection.city, connection.country, connection.reachable, connection.station_to,
                     connection.lat, connection.long])

    def update_track_file(self, from_city):
        '''
        creates a new dict with connections information and
        adds it to the existing track_file
        to be completed
        '''

    def count_reachables(self, track_dict: str, home_location):
        with open(track_dict, 'r') as f:
            j_object = json.loads(f.read())
            part = j_object[home_location]
            count_reach = 0
            count_unreach = 0
            for city in part:
                if city['access'] == 'reachable':
                    if city['x'] != 'null':
                        count_reach += 1
                else:
                    count_unreach += 1
        return (count_reach, count_unreach)


if __name__ == '__main__':
    t = TrackCities()
    t.create_track_file('Zürich')
    t.create_track_file('Genf')
    t.create_track_file('Bern')
    t.create_track_file('Basel')
    # reach_from_zürich = t.count_reachables('track_dict.json', 'Zürich')
    # print(reach_from_zürich)
