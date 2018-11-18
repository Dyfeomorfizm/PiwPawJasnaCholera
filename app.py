import fb
import scrapers


def run_scraper():
    jcs = scrapers.JasnaCholeraScraper()
    return jcs.run()


def check_where_is(bars):
    d = {
        "parkingowa": "nie wiem",
        "foksal": "nie wiem"
    }
    for key in d.keys():
        for bar in bars:
            if key in bar.lower():
                d[key] = "jest"
                break
        else:
            d[key] = "nie ma"
    return d


def create_msg(d):
    msg = "Dzisiaj na Parkingowej {}, na Foksal {}.".format(*d.values())
    return msg


def run_app():
    bars = run_scraper()
    d = check_where_is(bars)
    msg = create_msg(d)
    # fb.publish(msg)
    return msg


if __name__ == '__main__':
    run_app()