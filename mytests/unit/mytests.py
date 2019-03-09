import unittest
from unittest.mock import patch, MagicMock

from facebot.app import check_where_is, create_msg
from facebot.facebot.spiders.scrapers import JasnaCholeraScraper


class ParkingowaScraperTests(unittest.TestCase):
    def test_get_list_of_bars(self):
        mock = MagicMock(
            return_value=MagicMock(text=open('mytests/test_htmls/jasnacholera_test.html').read())
        )

        with patch('facebot.facebot.spiders.scrapers.JasnaCholeraScraper.get_response', mock):
            jcs = JasnaCholeraScraper()
            self.assertEqual(jcs.run(), ['Piw Paw ul.Foksal 16', 'Piw Paw ul. Piotrkowska 147'])


class AppTests(unittest.TestCase):
    def test_check_where_is(self):
        bars = ["Foksal", "Nowogrodzka", "Grzybowska"]
        d = check_where_is(bars)
        self.assertEqual(d["parkingowa"], "nie ma")
        self.assertEqual(d["foksal"], "jest")

    def test_create_msg(self):
        d = {"a": "jest", "b": "nie ma"}
        msg = create_msg(d)
        correct_msg = "Dzisiaj na Parkingowej jest, na Foksal nie ma."
        self.assertEqual(msg, correct_msg)


if __name__ == '__main__':
    unittest.main()
