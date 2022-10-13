import scrapy
from ..items import ScrpperItem

class AmazonScrp(scrapy.Spider):
    name='amazon'
    start_urls=[
        'https://www.amazon.in/s?k=samsung+galaxy+m02s'
    ]

    page_domain = "https://amazon.in"

    def parse(self, response):
        items = ScrpperItem()
        
        products = response.xpath('//div[@data-component-type="s-search-result"]')

        for product in products:
            product_link = AmazonScrp.page_domain+product.css('a.a-link-normal.s-no-outline').xpath('@href').get()
            product_image = product.css('a.a-link-normal.s-no-outline').xpath('div/img/@src').get()
            product_name = product.css('a.a-link-normal.s-no-outline').xpath('div/img/@alt').get()
            product_price_symb = product.css('span.a-price-symbol::text').get()
            product_price = product.css('span.a-price-whole::text').get()

            items['product_link'] = product_link
            items['product_image'] = product_image
            items['product_name'] = product_name
            items['product_price_symb'] = product_price_symb
            items['product_price'] = product_price


            yield items