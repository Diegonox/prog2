class Station:
    def __init__(self, city, reachable=False, station_to=None, lat=None, long=None):
        self.city = city
        self.reachable = reachable
        self.station_to = station_to
        self.lat = lat
        self.long = long
        