"""
@author: Diego Fontana
"""

import unittest
from services.subset_calculator import SubsetCalculator
from models.station import Station


class TestSubsetCalculator(unittest.TestCase):

    def test_calculator(self):
        station1 = Station()
        station1.city = 'Frankfurt'
        station1.reachable = True
        station1.lat = 1
        station1.long = 0.5
        station2 = Station()
        station2.city = 'Paris'
        station2.lat = -1
        station2.long = -1
        station_Zurich = Station()
        station_Zurich.city = 'Zurich'
        station_Zurich.lat = 0
        station_Zurich.long = 0
        station_Berlin = Station()
        station_Berlin.city = 'Berlin'
        station_Berlin.lat = 1
        station_Berlin.long = 1
        stations = [station1, station2]
        subset_calculator = SubsetCalculator()
        reachable_stations = subset_calculator.get_subset_stations_for_given_start_and_destination(stations,
                                                                            station_Zurich,
                                                                            station_Berlin)
        self.assertEqual(len(reachable_stations), 1)
        self.assertEqual(reachable_stations[0].city, 'Frankfurt')


if __name__ == '__main__':
    unittest.main()
