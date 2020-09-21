# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Job51CrawlSpider.items import Job51CrawlspiderItem
import re
import logging

class A51jobSpider(CrawlSpider):
    name = '51Job'
    allowed_domains = ['51job.com']
    start_urls = ['https://m.51job.com/search/joblist.php?keyword=Java+开发工程师&keywordtype=2&jobarea=040000&landmark=&issuedate=&saltype=&degree=&funtype=&indtype=&jobterm=&cotype=&workyear=&cosize=&lonlat=&tubename=&tubeline=&radius=&filttertype=']

    rules = (
        # LinkExtractor 连接提取器,提取url地址
        # callback 提取url地址的response会交给callback处理
        # follow 当前url地址的响应是否重新经过rules重新提取url地址
        #详情页的Rule规则
        Rule(LinkExtractor(allow=r'/jobs/shenzhen/\d+\.html\?jobtype=0'), callback='parse_item'),
        #下一页的Rule规则 这里有点问题
        # Rule(LinkExtractor(allow=r'<a href="(https://m\.51job\.com/search/joblist\.php\?jobarea=040000&amp;keyword=Java\+%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&amp;keywordtype=2&amp;pageno=\d+)" class="next"><i>下一页</i></a>'), follow=True),
    )

    # parse函数有特殊功能,不能定义
    def parse_item(self, response):
        item=Job51CrawlspiderItem()
         # 职位名称 ,例如中级开发工程师
        item["jobName"]=response.xpath("//div[@id='pageContent']/div[@class='mod m1']/div[@class='jt']/p/text()").extract_first()
        # 发布时间
        item["date"]=response.xpath("//div[@id='pageContent']/div[@class='mod m1']/div[@class='jt']/span/text()").extract_first()
        # 岗位jd-岗位jd有多余字符 ,需要处理
        item["jobRequest"]=response.xpath("//div[@id='pageContent']/div[@class='mod']/div[@class='ain']/article/p/text()").extract()
        # 上班地点
        # OK
        # item["jobErea"]=re.findall(">上班地址 : (.*?)<",response.body.decode())[0]
        # OK
        # item["jobErea"]=re.findall("上班地址 : (.*?)<",response.body.decode())[0]
        # 奶茶哥的建议
        # item["jobErea"]=re.findall("上班地址 : .+(?=<)",response.body.decode())[0]
        # 处理特殊字符
        item["jobRequest"]=[re.sub(r"\xa0|' '|\xa0|\s|\n","",i) for i in  item["jobRequest"]]
        # 处理空格
        item["jobRequest"]=[i for i in item["jobRequest"] if len(i)>0]
        yield item
