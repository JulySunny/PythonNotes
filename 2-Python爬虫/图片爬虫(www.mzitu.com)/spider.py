# coding=utf-8
# !/usr/bin/ env python
"""
图片爬虫,爬取www.mzitu.com网站的图片
"""
from bs4 import BeautifulSoup
import requests
import os

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip',
    "Referer": "https://www.mzitu.com/101553"
}  # 头部文件
os.system("mkdir jpg")
path = "jpg"  # jpg为保存目录，可随意更改
os.chdir(path)
now = os.getcwd()

url = 'https://www.mzitu.com'
response1 = requests.get(url, headers=headers)
html_soup1 = BeautifulSoup(response1.text, 'lxml')
all_url = html_soup1.find("ul", {"id": "pins"}).find_all("a")
count = 1
for href in all_url:
    count = count + 1
    if count % 2 != 0:
        href1 = href['href']
        # print(href1)
        for href2 in href:
            response2 = requests.get(href1, headers=headers)
            html_Soup2 = BeautifulSoup(response2.text, 'lxml')
            pic_address = html_Soup2.find("div", {"class": "main-image"}).find("img")['src']
            # print(pic_address)
            next_address = html_Soup2.find_all("span")[9]
            max_adress = next_address.get_text()
            name = html_Soup2.find("div", {"class": "main-image"}).find("img")['alt']
            os.mkdir(name)
            os.chdir(name)
            for i in range(1, int(max_adress) + 1):
                # print(i)
                next_url = href1 + '/' + str(i)
                response3 = requests.get(next_url, headers=headers)
                html_Soup3 = BeautifulSoup(response3.text, 'lxml')
                pic_address2 = html_Soup3.find("div", {"class": "main-image"}).find("img")['src']
                title = html_Soup3.find("h2")
                name1 = title.get_text()
                img = requests.get(pic_address2, headers=headers)
                f = open(name1 + '.jpg', 'ab')
                f.write(img.content)
                f.close()
            os.chdir(now)  # 获取自己的工作目录，将/Users/w2ng/untitled/venv 改为os.getcwd()的结果就ok
