import requests
from bs4 import BeautifulSoup

import facebot.facebot.spiders.scrapers as scrapers


def run_scraper():
    jcs = scrapers.JasnaCholeraScraper()
    return jcs.run()


def check_where_is(bars):
    d = {}
    for address in ["parkingowa", "foksal"]:
        for bar in bars:
            if address in bar.lower():
                d[address] = "jest"
                break
        else:
            d[address] = "nie ma"
    return d


def create_msg(d):
    msg = "Dzisiaj na Parkingowej {}, na Foksal {}.".format(*d.values())
    return msg


def run_app():
    bars = run_scraper()
    d = check_where_is(bars)
    msg = create_msg(d)
    return msg


def run_ania():
    websites = [
        [
            'https://ontap.pl/beer?mode=view&beer_id=6557',
            'https://ontap.pl/beer?mode=view&beer_id=15023',
            'https://ontap.pl/beer?mode=view&beer_id=19999',
            'https://ontap.pl/beer?mode=view&beer_id=12861',
            'https://ontap.pl/beer?mode=view&beer_id=12940',
            'https://ontap.pl/beer?mode=view&beer_id=12939',
        ],
        [
            'https://ontap.pl/beer?mode=view&beer_id=17745',
            'https://ontap.pl/beer?mode=view&beer_id=2056',
        ],
    ]

    names = ['Pan IPAni', "Double Pan IPAni"]
    msg = "Dzisiaj w Warszawce"
    for n, ws in zip(names, websites):
        bars = sum([get_bars(w) for w in ws], [])
        msg += mk_msg(n, bars)
        msg += "\n"
    msg = msg[:-1] + "."
    return msg


def mk_msg(n, bars):
    msg = " " + n + " "
    if len(bars):
        msg += "jest w "
        for b in bars:
            msg = msg + b + ", "
        msg = msg[:-1]
    else:
        msg += 'nie ma nigdzie,'
    return msg


def get_bars(w):
    r = requests.get(w)
    soup = BeautifulSoup(r.text, "lxml")
    bars = soup.find_all('div', class_=" col-xs-6")
    return [b.a.text for b in bars if 'Warszawa' in b.text]


if __name__ == '__main__':
    print(run_ania())
