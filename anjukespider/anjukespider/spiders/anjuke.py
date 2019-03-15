# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['xt.fang.anjuke.com']
    start_urls = ['https://xt.fang.anjuke.com/']

    def parse(self, response):
        pass

