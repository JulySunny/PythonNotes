# -*- coding: utf-8 -*-
import re

import scrapy

"""Scrapy模拟登录"""
# 1.使用scrapy.FormRequest(),发送post请求,需要你自己找到请求的url
# 2.使用scrapy.FormRequest.from_response(传递formdata表单请求项)
# AlenYang123456
# 7707191w
class GithubSpider(scrapy.Spider):

    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        """第一种方式:使用scrapy.FormRequest"""
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        timestamp=response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret=response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        webauthn_support=response.xpath("//input[@name='webauthn-support']/@value").extract_first()
        post_data = {
            "login":"AlenYang123456",
            "password":"7707191ww",
            "authenticity_token":authenticity_token,
            "webauthn-support":webauthn_support,
            "utf8":utf8,
            "timestamp":timestamp,
            "timestamp_secret":timestamp_secret,
            "required_field_2df7": "",
            "commit":commit
        }
        yield scrapy.FormRequest(
             #第一种方式:使用scrapy.FormRequest
            "https://github.com/session",
            formdata=post_data,
            callback=self.afer_login
        )
        yield scrapy.FormRequest.from_response(
             #第一种方式:使用scrapy.FormRequest
            "https://github.com/session",
            formdata=post_data,
            callback=self.afer_login
        )

    def afer_login(self,response):
        print(re.findall("AlenYang123456|alenYang123456",response.body.decode()))
        pass
