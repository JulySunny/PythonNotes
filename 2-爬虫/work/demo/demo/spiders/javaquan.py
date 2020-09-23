import scrapy
import logging


class JavaquanSpider(scrapy.Spider):
    name = 'javaquan'
    allowed_domains = ['javaquan.com']
    start_urls = ['http://javaquan.com/']

    def parse(self, response):
        pass
