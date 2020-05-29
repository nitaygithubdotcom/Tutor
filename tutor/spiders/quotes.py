# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quolen = '(//div[@class="quote"]/span[@class])'
        lngth = len(response.xpath(quolen))
        quote = '(//div[@class="quote"]/span[@class])[{}]/text()'
        author = '(//div[@class="quote"]/span[@class])[{}]/text()/../../span/small/text()'
        tags = '(//div[@class="quote"]/span[@class])[{}]/text()/../../span/small/text()/../../../div/a/text()'
        for i in range(lngth):
            q = quote.format(i+1)
            a = author.format(i+1)
            t = tags.format(i+1)
            quo = response.xpath(q).get()
            aut = response.xpath(a).get()
            tag = response.xpath(t).getall()
            data = {'Quotes':quo,'Author':aut,'Tags':tag}
            yield data
