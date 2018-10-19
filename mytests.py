import unittest
from unittest.mock import patch, MagicMock

from scrapers import ParkingowaScraper, FoksalScraper


class MyFirstTests(unittest.TestCase):

    def test_website(self):
        websites = [s.website for s in [ParkingowaScraper(), FoksalScraper()]]
        self.assertEqual(websites, ['http://piw-paw.ontap.pl/', 'http://piw-paw-foksal.ontap.pl/'])


class ParkingowaScraperTests(unittest.TestCase):
    def test_get_list_of_bears(self):
        mock = MagicMock(
            return_value=MagicMock(text=open('parkingowa_test.html').read())
        )

        with patch('scrapers.ParkingowaScraper.get_response', mock):
            ps = ParkingowaScraper()
            ps.run()
            self.assertEqual(ps.beers, [])


if __name__ == '__main__':
    unittest.main()
