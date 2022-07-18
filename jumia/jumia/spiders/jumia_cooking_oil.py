from gc import callbacks
import scrapy

class JumiaCookingOilSpider(scrapy.Spider):
    name = 'jumia_cooking_oil'
    allowed_domains = ['www.jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/catalog/?q=cooking+oil']

    def parse(self, response):
        for item in response.css('article.prd._fb.col.c-prd'):
            yield{
                'item_link': item.css('a.core::attr(href)').get(),
                'item_name': item.css('a.core::attr(data-name)').get(),
                'item_store': item.css('div.bdg._mall._xs::text').get(),
                'item_price': item.css('div.prc::text').get(),
                'item_discount': item.css('div.bdg._dsct::text').get(),
                'item_categ': item.css('a.core::attr(data-category)').get(),
                'item_img_url': item.css('img.img::attr(data-src)').get()
            }

        next_page = response.css('a.pg::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
        pass
