from geopy import Nominatim


class Station:
    def __init__(self):
        # city/name
        self.city = None
        self.country = None
        self.lat = None
        self.long = None
        self.reachable = False
        self.station_to = None

    def set_station_by_json(self, json_response):
        if json_response:
            self.set_station_by_city(json_response['name'])
            self.reachable = True
            self.long = json_response['coordinate']['y']
            self.lat = json_response['coordinate']['x']

    def set_station_by_csv(self, csv_row):
        if csv_row:
            self.city = csv_row[0]
            self.country = csv_row[1]
            self.reachable = csv_row[2]
            self.station_to = csv_row[3]
            if csv_row[4]:
                self.lat = float(csv_row[4])
            if csv_row[5]:
                self.long = float(csv_row[5])

    def set_station_by_city(self, city):
        if city:
            self.city = city
            locator = Nominatim(user_agent='p05')
            location = locator.geocode(self.city)
            self.country = location.address.split(', ')[-1]
            self.lat = location.latitude
            self.long = location.longitude

    def set_station_by_api_response(self, api_response):
        if api_response and api_response['connections'] != []:
            connection = api_response['connections']
            connection = connection[0]
            self.reachable = True
            self.station_to = connection['to']['station']['name']
            self.lat = connection['to']['station']['coordinate']['y']
            self.long = connection['to']['station']['coordinate']['x']
