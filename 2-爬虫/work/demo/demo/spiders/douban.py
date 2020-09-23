import logging

import scrapy
# from demo.items import DemoItem
from ..items import DemoItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        item = DemoItem()
        li_list = response.xpath("//div[@class='article']/ol[@class='grid_view']/li")
        item_list = []
        for li in li_list:
            item['name'] = li.xpath("./div[@class='item']//div[@class='pic']/a/img/@alt").extract_first()
            item['score'] = li.xpath(
                "./div[@class='item']/div[@class='info']//span[@class='rating_num']/text()").extract_first()
            item['detail'] = li.xpath("./div[@class='item']/div[@class='info']//p[1]/text()").extract_first().strip()
            item_list.insert(item)
        next_url=response.xpath("//div[@class='paginator'")
        yield scrapy.Request(

        )
