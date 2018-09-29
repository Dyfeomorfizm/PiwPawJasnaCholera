import requests
import lxml.etree


class PiwPawScraper(object):
    website = ''
    xpath = '//h4[contains(@class, "cml_shadow")]/span/text()'

    def __init__(self):
        self.parser = lxml.etree.HTMLParser()

    def get_response(self):
        return requests.get(self.website)

    def get_html_tree(self, response):
        response_bytes = bytes(bytearray(response.text, encoding='utf-8'))
        return lxml.etree.HTML(response_bytes, self.parser)

    def _get_list_of_beers(self, html_tree):
        return html_tree.xpath(self.xpath)

    def run(self):
        response = self.get_response()
        html_tree = self.get_html_tree(response)

        self.beers = self._get_list_of_beers(html_tree)


class ParkingowaScraper(PiwPawScraper):
    website = 'http://piw-paw.ontap.pl/'


class FoksalScraper(PiwPawScraper):
    website = 'http://piw-paw-foksal.ontap.pl/'
