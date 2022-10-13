# -*- coding: utf-8 -*-
import scrapy
from ..utils import clean_html, remove_html_tags, remove_tags


class TPSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['www.flipkart.com']
    # base_url = "https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-black-dusk-128-gb/p/itm7acae55b999e6?pid=MOBGHH9FVUHCFHTY&lid=LSTMOBGHH9FVUHCFHTYTOIZQW&marketplace=FLIPKART&q=oneplus&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=4516617c-e56d-4e46-bf00-c0756049da0d.MOBGHH9FVUHCFHTY.SEARCH&ppt=sp&ppn=sp&ssid=zijd388hn40000001663329024516&qH=43780d550576947f"
    # base_url = "https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-black-dusk-128-gb/p/itm7acae55b999e6"
    base_url = "https://www.flipkart.com/apple-iphone-14-product-red-128-gb/p/itm1f78a4e1a1d76"
    filename = 'flipkart'
    start_urls = [base_url]
    data_list = []

    def parse(self, response):
        print(response.url)
        # data = response.css('div._1AtVbE.col-12-12')
        data = response.css('div.aMaAEs')
        prodcut_name = data.css('span.B_NuCI::text').extract_first()
        print(prodcut_name)
        # print(remove_html_tags(prodcut_name))
        # print(prodcut_name[0])
        prodcut_price = data.css('div._30jeq3._16Jk6d::text').extract_first()
        print(prodcut_price)
        # print(remove_html_tags(prodcut_price))
        # print(prodcut_price[0])
        data = {'prodcut_name': prodcut_name, 'prodcut_price': prodcut_price}
        print('data --> ', data)
        yield data

