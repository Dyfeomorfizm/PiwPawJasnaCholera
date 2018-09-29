import requests
import lxml.etree


class BaseScraper(object):
    website = ''
    xpath = ''

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
        self.html_tree = self.get_html_tree(response)


class PiwPawScraper(BaseScraper):
    xpath = '//h4[contains(@class, "cml_shadow")]/span/text()'

    def run(self):
        super(PiwPawScraper, self).run()
        self.beers = self._get_list_of_beers(self.html_tree)


class ParkingowaScraper(PiwPawScraper):
    website = 'http://piw-paw.ontap.pl/'


class FoksalScraper(PiwPawScraper):
    website = 'http://piw-paw-foksal.ontap.pl/'


class JasnaCholeraScraper(BaseScraper):
    website = 'http://ontap.pl/beer?mode=view&&beer_id=455'
    xpath = '//*[@id="pubs"]/div/div[@class=" col-xs-6"]/a/text()'

    def run(self):
        super(JasnaCholeraScraper, self).run()
        results = self._get_list_of_bars(self.html_tree)

    def _get_list_of_bars(self, html_tree):
        return html_tree.xpath(self.xpath)

    def save(self):
        # TODO: SQLite
        pass


if __name__ == '__main__':
    f = JasnaCholeraScraper()
    f.run()
