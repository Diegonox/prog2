import countries


class Station:
    def __init__(self, city, api_response):
        self.city = city
        if api_response['connections']:
            connection = api_response['connections']
            connection = connection[0]
            self.reachable = True
            self.station_to = connection['to']['station']['name']
            self.lat = connection['to']['station']['coordinate']['x']
            self.long = connection['to']['station']['coordinate']['y']

        else:
            self.reachable = False
            self.station_to = None
            self.lat = None
            self.long = None
