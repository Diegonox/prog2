import math
from typing import List
from models.station import Station


class SubsetCalculator:
    """
    Get reachable connection stations, which should be within +/ 20° of the
    line of sight between start and destination.
    """

    @staticmethod
    def get_subset_stations_for_given_start_and_destination(stations: List[Station], start: Station,
                                                            destination: Station):
        """
        Get reachable connection stations, which should be within +/ 20° of the
        line of sight between start and destination.
        """
        reachable_stations = []
        start_dest_angle = math.degrees(
            math.atan2(destination.lat - start.lat, destination.long - start.long))
        for station in stations:
            station_dest_angle = math.degrees(math.atan2(station.lat - start.lat, station.long - start.long))
            if abs(station_dest_angle - start_dest_angle) <= 20:
                reachable_stations.append(station)
        return reachable_stations
