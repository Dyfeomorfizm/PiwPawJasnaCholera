import lxml.etree
import requests
import re


class BaseScraper(object):
    website = ''
    xpath = ''

    def __init__(self):
        self.html_tree = None
        self.parser = lxml.etree.HTMLParser()

    def get_response(self):
        return requests.get(self.website)

    def get_html_tree(self, response):
        response_bytes = bytes(response.text, encoding='utf-8')
        return lxml.etree.HTML(response_bytes, self.parser)

    def run(self):
        response = self.get_response()
        self.html_tree = self.get_html_tree(response)


class PiwPawScraper(BaseScraper):
    xpath = '//h4[contains(@class, "cml_shadow")]/span/text()'

    def __init__(self):
        super().__init__()
        self.beers = None

    def _get_list_of_beers(self, html_tree):
        for i in html_tree.xpath(self.xpath):
            i = re.sub('\s+', ' ', i.strip())

            if i and '%' not in i:
                yield i

    def run(self):
        super().run()
        self.beers = set(self._get_list_of_beers(self.html_tree))


class ParkingowaScraper(PiwPawScraper):
    website = 'https://piw-paw.ontap.pl/'


class FoksalScraper(PiwPawScraper):
    website = 'https://piw-paw-foksal.ontap.pl/'


class BeerScraper(BaseScraper):
    website = ''
    xpath = '//*[@id="pubs"]/div/div[@class=" col-xs-6"]/a/text()'

    def run(self):
        super().run()
        results = self._get_list_of_bars(self.html_tree)
        return results

    def _get_list_of_bars(self, html_tree):
        return html_tree.xpath(self.xpath)

    def save(self):
        # TODO: SQLite
        pass


class JasnaCholeraScraper(BeerScraper):
    website = 'https://ontap.pl/beer?mode=view&&beer_id=455'


class PanIPAniScraper(BeerScraper):
    website = 'https://ontap.pl/beer?mode=view&&beer_id=6557'


class DoublePanIPAniScraper(BeerScraper):
    website = 'https://ontap.pl/beer?mode=view&&beer_id=17745'


if __name__ == '__main__':
    f = JasnaCholeraScraper()
    f.run()
