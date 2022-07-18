### CSS Selectors

List of items => response.css('div.itm.col')
List of articles => response.css('article.prd._box._hvr')

item_link => response.css('a.core::attr(href)').get()
item_name => response.css('div.name::text').get()
item_price => response.css('div.prc::text').get()
item_discount => response.css('div.bdg._dsct::text').get()
item_categ => response.css('a.core::attr(data-category)').get()
item_img_url => response.css('img.img::attr(data-src)').get()