# -*- coding: utf-8 -*-
import copy

import scrapy
from WallPaperSpider.items import WallpaperspiderItem
import logging

class NetbianSpider(scrapy.Spider):
    """www.netbian.com全站图片爬虫"""
    name = 'netbian'
    allowed_domains = ['netbian.com']
    start_urls = ['http://www.netbian.com/']

    def parse(self, response):
        """按图片类型分组"""
        type_list=response.xpath("//div[@class='nav cate']/a")
        str="aaa"
        # 构造每种类型的壁纸URL
        type_list=["http://www.netbian.com"+i.xpath("./@href").extract_first() for i in type_list if "http" not in i.xpath("./@href").extract_first()]
        print("【所有类型图片列表】type_list========>>>>>%s"%type_list)
        for type in type_list:
            yield scrapy.Request(
                 type,                                    #传递的网页URL
                 callback=self.type_parse,                #传递的回调方法
            )
            pass
        pass

    def type_parse(self,response):
         """图片分组"""
         detail_list = response.xpath("//div[@class='list']/ul/li")
         for detail in detail_list:
             item=WallpaperspiderItem()
             # item = response.meta["item"]
             # 每个图片的详情页
             detail_page = detail.xpath("./a/@href").extract_first()
             if detail_page is not None:
                    detail_page = "http://www.netbian.com" + detail_page
                    yield scrapy.Request(
                            detail_page,
                            callback=self.parse_detail_page,
                            meta={"item": copy.deepcopy(item)}
                    )
         # 获取所有的a标签
         exist = response.xpath("//div[@class='page']/a[@class='prev']//text()").extract()
         next_url=""
         if len(exist) == 2:
            # next_page and  pre_page
            next_url=response.xpath("//div[@class='page']/a[@class='prev'][2]/@href").extract_first()
            next_url = "http://www.netbian.com" + next_url
         elif len(exist)==1 and response.xpath("//div[@class='page']/a[@class='prev']/text()").extract_first()=="下一页>":
            # only next_page
            next_url=response.xpath("//div[@class='page']/a[@class='prev']/@href").extract_first()
            next_url = "http://www.netbian.com" + next_url
         print("【下一页: URL ==>> %s】" %next_url)
         yield scrapy.Request(
                next_url,
                callback=self.type_parse
                )
         pass
    def parse_detail_page(self, response):
        """图片详情页解析"""
        item = response.meta["item"]
        # 获取下载页href-相对路径
        download_page = response.xpath("//div[@class='pic-down']/a/@href").extract_first()
        # 绝对路径
        if download_page is not None:
            download_page = "http://www.netbian.com" + download_page
            yield scrapy.Request(
                    download_page,
                    callback=self.parse_download_page,
                    # deepcopy
                    meta={"item": copy.deepcopy(item)}
            )

    def parse_download_page(self, response):
        """图片下载页解析,并传递下载URL到PIPLINE"""
        item = response.meta["item"]
        target_page = response.xpath("//table[@id='endimg']/tr/td/a/img/@src").extract_first()
        item["down_url"] = target_page
        logging.warning(item)
        yield item
