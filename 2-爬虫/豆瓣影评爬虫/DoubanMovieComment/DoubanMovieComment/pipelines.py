# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import logging
class DoubanmoviecommentPipeline(object):
    def __init__(self):
        self.client=MongoClient()
        self.collection = self.client["douban"]["comment"]
    def process_item(self, item, spider):
        logging.info(item)
        self.collection.insert(dict(item))
        return item
# bid=7SyqInA0X2A; ll="118282"; _vwo_uuid_v2=DB0CDD326BE76C1F029755619E5599D90|d201258ba073dcab2503b1a47b905be5; _ga=GA1.2.643835604.1560739348; viewed="26285268"; gr_user_id=3a9c1693-de26-4318-b6ec-3336c7a3d734; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1565675514%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6HpnIbRNaYHmumhoitSKKvZ76FukmHMYCN76rUl5y8ltmIsNCN1o8rTx4xT4UDr9%26wd%3D%26eqid%3Dadb143c6000fa88f000000065d524fed%22%5D; _pk_id.100001.8cb4=34839ef5e8790fcd.1565675514.1.1565675514.1565675514.; __yadk_uid=GcivoxSLAjHE2MY0AiE0DTkJwCy6Tffq; trc_cookie_storage=taboola%2520global%253Auser-id%3D91a73a2b-ba8d-4c28-9d3d-692535733e43-tuct411dac7; __utmz=30149280.1565711095.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; __utma=30149280.643835604.1560739348.1565754243.1565761654.10; __utmt=1; __utmc=30149280; ap_v=0,6.0; __utmb=30149280.8.9.1565761828355; dbcl2="201918819:6w5YXCY3+xM"

# bid=7SyqInA0X2A; ll="118282"; __yadk_uid=iz24NDKxQy3uVEHYxFzK78pyLCqdwoZv; _vwo_uuid_v2=DB0CDD326BE76C1F029755619E5599D90|d201258ba073dcab2503b1a47b905be5; _ga=GA1.2.643835604.1560739348; viewed="26285268"; gr_user_id=3a9c1693-de26-4318-b6ec-3336c7a3d734; __utmz=30149280.1565711095.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1565711095.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1565761654%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DUpNwWmAUnqvaX-whr4RHcZ1XGYxOr5mWdSNZgT1TGjR70tQsGSSxKYUbaxrHbiM2%26wd%3D%26eqid%3Dce0d6bae000172c6000000065d52daf0%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.643835604.1560739348.1565754243.1565761654.10; __utmt=1; __utma=223695111.823285827.1560739348.1565754244.1565761680.7; __utmb=223695111.0.10.1565761680; __utmc=30149280; ap_v=0,6.0; __utmc=223695111; _pk_id.100001.4cf6=e83bc1fa94a43629.1560739348.7.1565761962.1565754243.; dbcl2="201918819:6w5YXCY3+xM"; ck=XUMT; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20191; __utmb=30149280.11.9.1565762040232

# bid=7SyqInA0X2A; ll="118282"; __yadk_uid=iz24NDKxQy3uVEHYxFzK78pyLCqdwoZv; _vwo_uuid_v2=DB0CDD326BE76C1F029755619E5599D90|d201258ba073dcab2503b1a47b905be5; _ga=GA1.2.643835604.1560739348; viewed="26285268"; gr_user_id=3a9c1693-de26-4318-b6ec-3336c7a3d734; __utmz=30149280.1565711095.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1565711095.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1565761654%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DUpNwWmAUnqvaX-whr4RHcZ1XGYxOr5mWdSNZgT1TGjR70tQsGSSxKYUbaxrHbiM2%26wd%3D%26eqid%3Dce0d6bae000172c6000000065d52daf0%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.643835604.1560739348.1565754243.1565761654.10; __utma=223695111.823285827.1560739348.1565754244.1565761680.7; __utmb=223695111.0.10.1565761680; ap_v=0,6.0; dbcl2="201918819:6w5YXCY3+xM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20191; __utmb=30149280.11.9.1565762040232; _pk_id.100001.4cf6=e83bc1fa94a43629.1560739348.7.1565762158.1565754243.