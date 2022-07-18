#### Whisky CSS

Next page => response.css('a.page::attr(href)').get()
Item list => response.css('li.item.product.product-item')

'item_url':response.css('a.product.photo.product-item-photo::attr(href)').get()
'item_name':response.css('a.product.photo.product-item-photo::attr(data-name)').get()
'item_store':response.css('a.product.photo.product-item-photo::attr(data-store)').get()
'item_img_url':response.css('img.product-image-photo::attr(src)').get()
'item_price':response.css('span.price::text').get()
