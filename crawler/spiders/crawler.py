import scrapy
import js2py
from scrapy import Selector, Request
import sys
import importlib
importlib.reload(sys)


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'

    def __init__(self, urls=None, items={},**kwargs):
        super(CrawlerSpider, self).__init__(**kwargs)
        self.start_urls = urls.split(",")
        self.items = items

    def start_requests(self):
        start_urls = self.start_urls
        return [Request(url=start_url) for start_url in start_urls]

    def parse(self, response):

        return self.items
