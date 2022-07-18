import scrapy


class JumiaHmpgSpider(scrapy.Spider):
    name = 'jumia_hmpg'
    allowed_domains = ['jumia.co.ke']
    start_urls = ['http://jumia.co.ke/']

    def parse(self, response):
        pass
