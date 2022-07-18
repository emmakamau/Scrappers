import scrapy

class JumiaHmpgSpider(scrapy.Spider):
    name = 'jumia_hmpg'
    allowed_domains = ['jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/']

    def parse(self, response):

        for item in response.css('article.prd._box._hvr'):
            yield{
                'item_link': item.css('a.core::attr(href)').get(),
                'item_name': item.css('div.name::text').get(),
                'item_price': item.css('div.prc::text').get(),
                'item_discount': item.css('div.bdg._dsct::text').get(),
                'item_categ': item.css('a.core::attr(data-category)').get(),
                'item_img_url': item.css('img.img::attr(data-src)').get()
            }
            
        pass
