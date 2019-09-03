# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviecommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user=scrapy.Field()     #评论用户
    date=scrapy.Field()     #评论时间
    content=scrapy.Field()  #评论内容
    level=scrapy.Field()    #评价等级
    votes=scrapy.Field()    #赞同数量
    pass
