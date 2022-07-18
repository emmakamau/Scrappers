import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/catalogsearch/result/?q=whisky']

    def parse(self, response):
        for item in response.css('li.item.product.product-item'):
            yield{
                'item_url':item.css('a.product.photo.product-item-photo::attr(href)').get(),
                'item_name':item.css('a.product.photo.product-item-photo::attr(data-name)').get(),
                'item_store':item.css('a.product.photo.product-item-photo::attr(data-store)').get(),
                'item_img_url':item.css('img.product-image-photo::attr(src)').get(),
                'item_price':item.css('span.price::text').get()
            }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        pass
