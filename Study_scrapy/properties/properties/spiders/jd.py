# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,Join
from scrapy.loader import ItemLoader
class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672']

    def parse(self, response):
        loader = ItemLoader(item=PropertiesItem(),response=response)
        html = response.selector.css('.clearfix >li')
        print(len(html))
        for i in html:
            loader.add_css('img_url','.p-img img')
            # item['img_url'] = i.css('.p-img img::attr("src")').extract_first()
            # item['price'] = i.css('.p-price i::text').extract_first()
            # item['name'] = i.css('.p-name em::text').extract_first()
            # item['commit'] = i.css('.p-commit-n strong::text').extract_first()
            # item['shop'] = i.css('.p-shop a::text').extract_first()
            # item['icons'] = i.css('.J-pro-icons i::text').extract_first()
            yield loader.load_item()