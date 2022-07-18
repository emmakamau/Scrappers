import scrapy


class JumiaCookingOilSpider(scrapy.Spider):
    name = 'jumia_cooking_oil'
    allowed_domains = ['www.jumia.co.ke']
    start_urls = ['http://www.jumia.co.ke/']

    def parse(self, response):
        pass
