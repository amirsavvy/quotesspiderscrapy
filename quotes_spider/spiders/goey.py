# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from quotes_spider.items import GoeySpiderItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class GoeySpider(Spider):
    name = 'goey'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token =  response.xpath('//*[@name="csrf_token"]/@value').extract_first()

        return FormRequest.from_response(response,
        """
        for form request use this function like login
        """
         formdata={'csrf_token': token,'username': 'amirsavvy','password': 'amirsavvy'},
         callback=self.scrape_home_page)

    def scrape_home_page(self, response):

        """
        For checking and debugging use this function
        to check which pages are scrapped
        """

        open_in_browser(response)

        l = ItemLoader(item=GoeySpiderItem(), response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags =  response.xpath('//*[@class="tag-item"]/a/text()').extract()
        tags_len = len(response.xpath('//*[@class="tag-item"]/a/text()').extract())
        # yield { 'H1 Tag': h1_tag, 'Tags': tags, 'Tags Length': tags_len }

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)
        l.add_value('tags_len', tags_len)

        return l.load_item()
