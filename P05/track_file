import requests
import json

"""
Call transport.opendata.ch api to get the connections between two locations.
"""



class TransportApiService:
    def __init__(self):
        self.base_api_url = 'https://transport.opendata.ch/v1/'
        self.connections_api_url = self.base_api_url + 'connections'
        self.connections_api_params = {
            'from': '',
            'to': '',
        }
        self.cities = ['Salzburg','Graz',
            'Bregenz', 'Feldkirch','Dornbirn','Vienne',
            'Frankfurt am Main','Köln','Wallhausen',
            'Ulm','Stuttgart Hbf','Freiburg im Breisgau','Bodman-Ludwigshafen',
            'Hamburg','Konstanz','Ravensburg', 'Karlsruhe',
            'Arnhem','Amsterdam','Venlo','Den Haag',
            'Paris','Lyon','Marseille','Mühlhausen',
            'Besançon','Grenoble','Nice','Charleroi',
            'London','Manchester','Liverpool','Birmingham','Leeds',
            'Prag',
            'Dublin','Belfast','Glasgow',
            'Cadaqués', 'Málaga','Murcia','Valencia',
            'Madrid','Saragosa','Barcelona','Bilbao','Valladolid',
            'Milano','Bologna', 'Aosta', 'Domodossola','como', 'Varese']
    
    def get_connections(self, from_location, to_location):
        self.connections_api_params['from'] = from_location
        self.connections_api_params['to'] = to_location
        try:
            r = requests.get(self.connections_api_url,
                             params=self.connections_api_params)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as err:
            print(err)
        except requests.exceptions.RequestException as e:
            print(e)
            return e
        
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
        dic_string = json.dumps(track_file, indent=2)

        with open ('track_dict', 'w') as f:
            f.write(dic_string)
            
            
            
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
        print ('reachable = ', count_reach, '\n', 'unreachable = ', count_unreach)


if __name__ == '__main__':
    

    t = TransportApiService()
    file = t.create_track_file('Zürich')
