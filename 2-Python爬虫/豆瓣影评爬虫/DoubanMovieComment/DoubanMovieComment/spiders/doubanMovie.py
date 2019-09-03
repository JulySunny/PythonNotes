# -*- coding: utf-8 -*-
import scrapy
from DoubanMovieComment.items import DoubanmoviecommentItem
import re

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanMovie' #哪吒-魔童降世短评爬虫
    allowed_domains = ['douban.com'] #站点
    start_urls = ['https://movie.douban.com/subject/26794435/comments?start=0&limit=20&sort=new_score'] #起始爬取页面


    def start_requests(self): #重构start_request 模拟登录后的状态
        cookies_str='bid=7SyqInA0X2A; ll="118282"; __yadk_uid=iz24NDKxQy3uVEHYxFzK78pyLCqdwoZv; _vwo_uuid_v2=DB0CDD326BE76C1F029755619E5599D90|d201258ba073dcab2503b1a47b905be5; _ga=GA1.2.643835604.1560739348; viewed="26285268"; gr_user_id=3a9c1693-de26-4318-b6ec-3336c7a3d734; __utmz=30149280.1565711095.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1565711095.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1565761654%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DUpNwWmAUnqvaX-whr4RHcZ1XGYxOr5mWdSNZgT1TGjR70tQsGSSxKYUbaxrHbiM2%26wd%3D%26eqid%3Dce0d6bae000172c6000000065d52daf0%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.643835604.1560739348.1565754243.1565761654.10; __utma=223695111.823285827.1560739348.1565754244.1565761680.7; __utmb=223695111.0.10.1565761680; ap_v=0,6.0; dbcl2="201918819:6w5YXCY3+xM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20191; __utmb=30149280.11.9.1565762040232; _pk_id.100001.4cf6=e83bc1fa94a43629.1560739348.7.1565762158.1565754243.'
        cookies_dict={i.split("=")[0]:i.split("=")[1] for i in cookies_str.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict
        )

    def parse(self, response):
        """1.对响应结果分组"""
        print("开始爬取")
        comment_list=response.xpath("//div[@id='comments']/div[@class='comment-item']") #获取评论集合
        item=DoubanmoviecommentItem()
        for comment in comment_list:
            # 评论人
            item["user"]=comment.xpath("./div[@class='comment']//span[@class='comment-info']/a/text()").extract_first()
            # 评论时间
            item["date"]=comment.xpath("./div[@class='comment']/h3/span[@class='comment-info']/span[@class='comment-time ']/text()").extract_first()
            # 评价等级
            item["level"]=comment.xpath("./div[@class='comment']/h3/span[@class='comment-info']/span[contains(@class,'rating')]/@title").extract_first()
            # item["level"]=re.findall("title=(.*?)>",comment.)[0]
            # 赞同数量
            item["votes"]=comment.xpath("./div[@class='comment']/h3/span[@class='comment-vote']/span[@class='votes']/text()").extract_first()
            # 评论内容
            item["content"]=comment.xpath("./div[@class='comment']/p/span[@class='short']/text()").extract_first()
            # 传递数据给Pipline去处理数据
            print(item)
            yield item
        # 下一页的url
        next_url=response.xpath("//div[@id='paginator']/a[@class='next']/@href").extract_first()
        if next_url is not None:
            next_url="https://movie.douban.com/subject/26794435/comments"+next_url
        print("下一页的 url============> %s"%next_url)
        yield scrapy.Request(
            next_url,
            callback=self.parse
        )
        pass
