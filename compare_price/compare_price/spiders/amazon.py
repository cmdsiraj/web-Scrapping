# -*- coding: utf-8 -*-
import scrapy
from ..utils import clean_html, remove_html_tags, remove_tags


class TPSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    # base_url = "https://www.amazon.in/OnePlus-Moonstone-Black-256GB-Storage/dp/B0B5V2SHGL/ref=cs_sr_dp_2?keywords=oneplus%2B10t&qid=1663321773&sprefix=oneplus%2B10t%2Caps%2C310&sr=8-1&th=1"
    # base_url = "https://www.amazon.in/OnePlus-Nord-Black-128GB-Storage/dp/B09WQY65HN"
    base_url = "https://www.amazon.in/Apple-iPhone-14-128GB-Blue/dp/B0BDK62PDX"
    filename = 'amazon'
    start_urls = [base_url]
    data_list = []

    def parse(self, response):
        print(response.url)
        data = response.css('div#centerCol')
        prodcut_name = data.css('span#productTitle::text').extract_first()
        if prodcut_name:
            print(remove_html_tags(prodcut_name))
        # print(prodcut_name[0])
        # prodcut_price = data.css('span.a-offscreen::text').extract_first()
        prodcut_price = data.css('span.a-price-whole::text').extract_first()
        if prodcut_price:
            print(prodcut_price)
            # print(remove_html_tags(prodcut_price))
        # print(prodcut_price[0])
        data = {'prodcut_name': remove_html_tags(prodcut_name), 'prodcut_price': prodcut_price}
        if data:
            print('data --> ', data)
        yield data

