from geopy import Nominatim


class Station:
    def __init__(self, city):
        self.city = city
        locator = Nominatim(user_agent='p05')
        location = locator.geocode(self.city)
        self.country = location.address.split(',')[-1]
        self.lat = location.latitude
        self.long = location.longitude
        self.reachable = False
        self.station_to = None

    def set_station_by_api_response(self, api_response):
        if api_response['connections']:
            connection = api_response['connections']
            connection = connection[0]
            self.reachable = True
            self.station_to = connection['to']['station']['name']
            self.lat = connection['to']['station']['coordinate']['x']
            self.long = connection['to']['station']['coordinate']['y']
