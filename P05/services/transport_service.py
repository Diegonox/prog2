import csv
import os

from models import Station
from .percentage_traveled import DistanceCalculator
from .response_types import ERROR, DIRECT_CONNECTION, NO_DIRECT_CONNECTION
from .transport_api_service import TransportApiService
from .subset_calculator import SubsetCalculator

__all__ = ['TransportService']


class TransportService:
    def __init__(self):
        self.transport_api_service = TransportApiService()
        self.subset_calculator = SubsetCalculator()
        self.distance_calculator = DistanceCalculator()

    def get_connections(self, start_location, destination_location):
        # blacklist check

        # if start doesn't exist return error
        start_location = start_location.title()
        destination_location = destination_location.title()
        start_station = self.transport_api_service.get_station(start_location)
        if not start_station:
            return 'Start location does not exist', ERROR

        destination_station = self.transport_api_service.get_station(destination_location)
        if not destination_station:
            return 'Destination location does not exist', ERROR

        # query to transport api
        # if destination reachable api response
        connection = self.transport_api_service.get_connections(start_station.city, destination_station.city)
        if connection['connections']:
            return connection['connections'], DIRECT_CONNECTION

        # if no connections query subset calculator
        stations = self.get_stations_for_given_start_location_from_track_file(start_station)
        if stations:
            reachable_stations = self.subset_calculator.get_subset_stations_for_given_start_and_destination(stations,
                                                                                                            start_station,
                                                                                                            destination_station)

            # if no connections query percentage travel
            result = self.distance_calculator.calculate_closest_location(reachable_stations,destination_station,start_station)
            return result, NO_DIRECT_CONNECTION
        return 'Can not give recommendation for this connection', ERROR

    @staticmethod
    def get_stations_for_given_start_location_from_track_file(start_station):
        if os.path.exists(f'../data/track_{start_station.city}.csv'):
            stations = []
            with open(f'../data/track_{start_station.city}.csv', 'r', encoding='utf8') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    station = Station()
                    station.set_station_by_csv(row)
                    stations.append(station)
            return stations
        return None
