# -*- coding: utf-8 -*-
import scrapy


class AmirSpider(scrapy.Spider):
    name = 'amir'
    allowed_domains = ['goey.co']
    start_urls = ['http://goey.co/']

    def parse(self, response):
        pass
