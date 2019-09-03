# -*- coding: utf-8 -*-
import scrapy
from suncrawl.items import SuncrawlItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        print("hello"*10)
        # 分组
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        # print("tr_list :::::::::::::::::::: %s "%tr_list)
        for tr in tr_list:
            item = SuncrawlItem()
            item["title"] = tr.xpath("./td[2]//a[@class='news14']/@title").extract_first()
            # print(item["title"])
            item["href"] = tr.xpath("./td[2]//a[@class='news14']/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[last()]/text()").extract_first()
            # print("临时输出数据 ::::::  %s" %item)

            yield scrapy.Request(
                    # 1.url
                    item["href"],
                    # 2.回调的方法 注意:方法后面不能有括号,否则就变成调用方法了
                    callback=self.parse_detail,
                    # 3.通过meta 传递数据 这里的"item" 是自己定义的key  可以随便定义
                    meta={"item": item}
            )

    def parse_detail(self, response):  # 处理详情页
        # 通过meta 字段拿到item 的值
        item = response.meta["item"]
        item["content"] = response.xpath("//td[@class='txt16_3']//text()").extract()
        item["content_img"] = response.xpath("//td[@class='txt16_3']//img/@src").extract()
        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        print(item)
