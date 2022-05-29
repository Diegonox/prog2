import json
from transport_api_service import TransportApiService


"""
Call transport.opendata.ch api to get the connections between two locations.
"""

class TrackFile:
    def __init__(self):
        self.cities = ['Salzburg','Graz',
            'Bregenz', 'Feldkirch','Dornbirn','Vienne',
            'Frankfurt am Main','Köln','Wallhausen',
            'Ulm','Stuttgart Hbf','Freiburg im Breisgau','Bodman-Ludwigshafen',
            'Hamburg','Konstanz','Ravensburg', 'Karlsruhe',
            'Arnhem','Amsterdam','Venlo','Den Haag',
            'Paris','Lyon','Marseille','Mühlhausen',
            'Besançon','Grenoble','Nice','Charleroi','Toulouse', 'Nancy',
            'London','Manchester','Liverpool','Birmingham','Leeds',
            'Prag',
            'Dublin','Belfast','Glasgow',
            'Cadaqués', 'Málaga','Murcia','Valencia',
            'Madrid','Saragosa','Barcelona','Bilbao','Valladolid',
            'Milano','Bologna', 'Aosta', 'Domodossola','como', 'Varese']
        
    def create_track_file(self, city_from):
        '''
        creates a json file called 'track_dict' with the connections from the 
        city_from to the cities in the list cities and defines the access as 
        reachable or unreachable
        '''
        track_file = {}
        prov_file = {}
        for city in self.cities:
            result = TransportApiService().get_connections(city_from, city)
            if result['connections'] == []:
                prov_file[city] = {'access':'unreachable'}
            else:
                result1 = result['connections']
                result2 = result1[0]
                s_from = result2['from']['station']['name']
                s_to = result2['to']['station']['name']
                lat = result2['to']['station']['coordinate']['x']
                long = result2['to']['station']['coordinate']['y']
                prov_file[city] = {'access': 'reachable','x':lat,'y':long, 'station_to':s_to}
        track_file[city_from] = prov_file
        dic_string = json.dumps(track_file, indent=4)

        with open ('track_dict.json', 'w') as f:
            f.write(dic_string)
            

    def update_track_file(self, from_city):

        ''' creates a new dict with connections information and
        adds it to the existing track_file
        '''
# to be completed

            
    def count_reachables(self, track_dict:str, home_location):
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
    

    t = TrackFile()
    t.create_track_file('Zürich')
    #reach_from_zürich = t.count_reachables('track_dict.json', 'Zürich')
    #print(reach_from_zürich)

