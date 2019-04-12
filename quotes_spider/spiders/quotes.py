# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # h1_tag = response.xpath('//h1/a/text()').extract_first()
        # tags =  response.xpath('//*[@class="tag-item"]/a/text()').extract()
        # tags_len = len(response.xpath('//*[@class="tag-item"]/a/text()').extract())
        # yield { 'H1 Tag': h1_tag, 'Tags': tags, 'Tags Length': tags_len }
        #

        """
        More adv spider script for quotstoscrape.com
        """

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            yield {'Text': text,
                    'Author': author,
                    'Tags' : tags
                    }

            next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
            absolute_next_page_url = response.urljoin(next_page_url)

            """
            Now request to the absolute_next_page_url i.e
            'http://quotes.toscrape.com/page/2/' (for 2nd page)
            """
            yield scrapy.Request(absolute_next_page_url)
