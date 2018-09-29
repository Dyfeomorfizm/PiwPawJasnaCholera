import unittest
from scrapers import Scraper

class MyFirstTests(unittest.TestCase):

    def test_scraper(self):
        website = 'http://www.example.com'
        s = Scraper()
        self.assertEqual(s.website, 'http://www.example.com')
