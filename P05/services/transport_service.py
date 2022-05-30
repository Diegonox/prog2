import csv

from models import Station
from .response_types import ERROR, DIRECT_CONNECTION
from .transport_api_service import TransportApiService
from .subset_calculator import SubsetCalculator

__all__ = ['TransportService']


class TransportService:
    def __init__(self):
        self.transport_api_service = TransportApiService()
        self.subset_calculator = SubsetCalculator()

    def get_connections(self, start_location, destination_location):
        # blacklist check

        # if start doesn't exist return error
        start_location = start_location.title()
        destination_location = destination_location.title()
        if not self.check_if_location_exists(start_location):
            return 'Start location does not exist', ERROR
        if not self.check_if_location_exists(destination_location):
            return 'Destination location does not exist', ERROR

        # query to transport api
        # if destination reachable api response
        if connection := self.transport_api_service.get_connections(start_location, destination_location):
            return connection, DIRECT_CONNECTION
        # if no connections query subset calculator
        stations = self.get_stations_for_given_start_location_from_track_file(start_location)
        reachable_stations = self.subset_calculator.get_subset_stations_for_given_start_and_destination(stations,
                                                                                                        start_location,
                                                                                                        destination_location)
        # if no connections query percentage travel

    def check_if_location_exists(self, location):
        if self.transport_api_service.get_location(location):
            return True
        return False

    @staticmethod
    def get_stations_for_given_start_location_from_track_file(start_location):
        stations = []
        with open(f'track_{start_location}.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                station = Station()
                station.set_station_by_csv(row)
                stations.append(station)
        return stations
