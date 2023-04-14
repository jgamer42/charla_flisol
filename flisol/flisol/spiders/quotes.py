from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[contains(@class,'quote')]"):
            yield self.get_quote_info(quote)
        next_page = response.xpath("//li[contains(@class,'next')]/a[@href]/@href").get()
        if next_page is not None:
            yield response.follow(next_page,self.parse)
            
    def get_quote_info(self,quote):
        return {
            "quote":quote.xpath("span[contains(@class,'text')]/text()").get(),
            "autor":quote.xpath("span/small/text()").get(),
            "tags":quote.xpath("div/a/text()").getall()
            }
    