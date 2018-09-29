import unittest
from scrapers import ParkingowaScraper, FoksalScraper

class MyFirstTests(unittest.TestCase):

    def test_website(self):
        websites = [s.website for s in [ParkingowaScraper(), FoksalScraper()]]
        self.assertEqual(websites, ['http://piw-paw.ontap.pl/', 'http://piw-paw-foksal.ontap.pl/'])
