# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request


class WallpaperspiderPipeline(object):
    def process_item(self, item, spider):
        if not os.path.exists("./AllWallPaper"):
            os.mkdir("./AllWallPaper")
        url=item["down_url"]
        if url is not None:
            print("url====>>%s" %url)
            name=str(url).split("/")[-1]
            with urllib.request.urlopen(url, timeout=30) as response, open("./AllWallPaper/" + name, "wb") as f:
                f.write(response.read())
                f.flush()
                f.close()
            print("图片下载成功")
        return item
