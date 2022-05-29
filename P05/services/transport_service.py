from .transport_api_service import TransportApiService
from .subset_calculator import SubsetCalculator


class TransportService:
    def __init__(self):
        self.transport_api_service = TransportApiService()
        self.subset_calculator = SubsetCalculator()

    def get_connections(self, start_location, destination_location):
        # blacklist check
        # query to transport api
        # if start doesn't exist return error
        # if destination reachable api response
        # if destination not reachable query subset calculator
        # if destination not reachable query percentage travel
        connections = self.transport_api_service.get_connections(start_location, destination_location)
        return self.subset_calculator.get_subset_stations_for_given_start_and_destination(connections, start_location,
                                                                                          destination_location)
