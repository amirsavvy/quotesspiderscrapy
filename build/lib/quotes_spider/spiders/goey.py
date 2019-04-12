# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from quotes_spider.items import GoeySpiderItem

class GoeySpider(Spider):
    name = 'goey'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=GoeySpiderItem(), response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags =  response.xpath('//*[@class="tag-item"]/a/text()').extract()
        tags_len = len(response.xpath('//*[@class="tag-item"]/a/text()').extract())
        # yield { 'H1 Tag': h1_tag, 'Tags': tags, 'Tags Length': tags_len }

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)
        l.add_value('tags_len', tags_len)

        return l.load_item()
