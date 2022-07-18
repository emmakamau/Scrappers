import scrapy


class JumiaCookingOilSpider(scrapy.Spider):
    name = 'jumia_cooking_oil'
    allowed_domains = ['www.jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/catalog/?q=Cooking+oil']

    def parse(self, response):
        pass
