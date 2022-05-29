import unittest
from ..services.subset_calculator import SubsetCalculator
from models.station import Station


class TestSubsetCalculator(unittest.TestCase):

    def test_calculator(self):
        stations = [Station('Frankfurt', lat=1, long=0.5), Station('Paris', lat=-1, long=-1)]
        subset_calculator = SubsetCalculator()
        reachable_stations = subset_calculator.get_subset_stations_for_given_start_and_destination(stations,
                                                                            Station('Zürich', lat=0, long=0),
                                                                            Station('Berlin', lat=1, long=1))
        self.assertEqual(len(reachable_stations), 1)
        self.assertEqual(reachable_stations[0].city, 'Frankfurt')


if __name__ == '__main__':
    unittest.main()
