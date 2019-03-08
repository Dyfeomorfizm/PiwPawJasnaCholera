from scrapy.http import FormRequest
import scrapy
import app


class FacebookSpider(scrapy.Spider):
    name = "fb_text"

    allowed_domains = ["mbasic.facebook.com"]

    def __init__(self, email='', password='', **kwargs):
        super().__init__(**kwargs)

        self.dict = {}
        self.email = email
        self.password = password
        self.names = []
        self.texts = []
        self.times = []

        self.start_urls = ['https://mbasic.facebook.com']

    def parse(self, response):
        return FormRequest.from_response(
            response,
            formxpath='//form[contains(@action, "login")]',
            formdata={'email': self.email, 'pass': self.password},
            callback=self.go_to_fanpage
        )

    def go_to_fanpage(self, response):
        href = 'https://mbasic.facebook.com/Czy-w-PiwPaw-jest-Jasna-Cholera-354252548451865'
        return scrapy.Request(url=href, callback=self.parse_fanpage_form, )

    def parse_fanpage_form(self, response):
        msg = app.run_app()
        return FormRequest.from_response(
            response,
            formxpath='//form[contains(@action, "composer")]',
            formdata={'xc_message': msg},
            callback=self.go_to_fanpage_2,
        )

    def go_to_fanpage_2(self, response):
        href = 'https://mbasic.facebook.com/panipanipiwoani'
        return scrapy.Request(url=href, callback=self.parse_fanpage_form_2, )

    def parse_fanpage_form_2(self, response):
        msg = app.run_ania()
        return FormRequest.from_response(
            response,
            formxpath='//form[contains(@action, "composer")]',
            formdata={'xc_message': msg},
        )
