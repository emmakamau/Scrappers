import scrapy


class GiftHampersSpider(scrapy.Spider):
    name = 'gift_hampers'
    allowed_domains = ['www.montyskenya.com']
    start_urls = ['http://www.montyskenya.com/']

    def parse(self, response):
        pass
