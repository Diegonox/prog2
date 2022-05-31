import unittest
from ..main.track_cities import TrackCities


class TestTrackCities(unittest.TestCase):

    def test_track_cities(self):

        self.cities = ['Salzburg', 'Graz',
                       'Bregenz', 'Feldkirch', 'Dornbirn', 'Vienne',
                       'Frankfurt am Main', 'Köln', 'Wallhausen',
                       'Ulm', 'Stuttgart Hbf', 'Freiburg im Breisgau', 'Bodman-Ludwigshafen',
                       'Hamburg', 'Konstanz', 'Ravensburg', 'Karlsruhe',
                       'Arnhem', 'Amsterdam', 'Venlo', 'Den Haag',
                       'Paris', 'Lyon', 'Marseille', 'Mühlhausen',
                       'Besançon', 'Grenoble', 'Nice', 'Charleroi',
                       'London', 'Manchester', 'Liverpool', 'Birmingham', 'Leeds',
                       'Prag',
                       'Dublin', 'Belfast', 'Glasgow',
                       'Cadaqués', 'Málaga', 'Murcia', 'Valencia',
                       'Madrid', 'Saragosa', 'Barcelona', 'Bilbao', 'Valladolid',
                       'Milano', 'Bologna', 'Aosta', 'Domodossola', 'como', 'Varese']

        self.city_from = 'Zurich'


        self.assertEqual()
        self.assertEqual()
        

if __name__ == '__main__':
    unittest.main()