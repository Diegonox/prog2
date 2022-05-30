import requests

__all__ = ['TransportApiService']

from models import Station


class TransportApiService:
    """
    Call transport.opendata.ch api to get the connections between two locations.
    """
    def __init__(self):
        self.base_api_url = 'https://transport.opendata.ch/v1/'
        self.location_api_url = self.base_api_url + 'locations'
        self.location_api_params = {'query': ''}

        self.connections_api_url = self.base_api_url + 'connections'
        self.connections_api_params = {
            'from': '',
            'to': '',
        }

    def get_station(self, location):
        self.location_api_params['query'] = location
        try:
            r = requests.get(self.location_api_url, params=self.location_api_params)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            try:
                station = Station()
                station.set_station_by_json(r.json()['stations'][0])
                return station
            except:
                return None
        except requests.exceptions.HTTPError as err:
            print(err)
        except requests.exceptions.RequestException as e:
            print(e)
            return e

    def get_connections(self, from_location, to_location):
        self.connections_api_params['from'] = from_location
        self.connections_api_params['to'] = to_location
        try:
            r = requests.get(self.connections_api_url, params=self.connections_api_params)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.json()
        except requests.exceptions.HTTPError as err:
            print(err)
        except requests.exceptions.RequestException as e:
            print(e)
            return e
